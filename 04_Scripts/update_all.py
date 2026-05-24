import os
import re

print("Iniciando a atualização em massa...")

# Caminhos dinâmicos baseados no diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
puml_dir = os.path.abspath(os.path.join(script_dir, "..", "03_Artefatos_Gerados"))
artifact_path = os.path.abspath(os.path.join(script_dir, "..", "01_Relatorios_e_Dashboard", "fluxos_casos_uso.md"))
astah_dir = os.path.abspath(os.path.join(script_dir, "..", "02_Modelagem_UML_Astah"))

# 1. Update attributes from public (+) to private (-) in UC*_Classe.puml files
if os.path.exists(puml_dir):
    for filename in os.listdir(puml_dir):
        if filename.startswith("UC") and filename.endswith("_Classe.puml"):
            filepath = os.path.join(puml_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Regex to find lines like `    +nome : string` and change to `    -nome : string`
            # But don't match lines with `(` which are methods
            new_lines = []
            for line in content.split('\n'):
                # Simple check: if it has '+' and ':' and no '(', it's likely an attribute
                if '+' in line and ':' in line and '(' not in line:
                    line = line.replace('+', '-', 1)
                new_lines.append(line)
            
            new_content = '\n'.join(new_lines)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Atualizado: {filename} (Atributos privados)")
        
        # Also update the IA in the global sequence diagram if present
        if filename == "Diagrama_Sequencia_Global.puml":
            filepath = os.path.join(puml_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            # If there's an <<Entidade>> that should be <<Control>>, we fix it
            new_content = content.replace("<<Entidade>> as IA", "<<Control>> as IA")
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Atualizado: {filename} (IA <<Control>>)")

# 2. Inject Flows into README.mds
# First, let's load the flows from the local flows_casos_uso.md
flows_dict = {}
if os.path.exists(artifact_path):
    with open(artifact_path, 'r', encoding='utf-8') as f:
        artifact_content = f.read()
    
    # Parse the artifact to extract flows per UC
    # Format is: ### UC01 - Title \n - **Fluxo Normal:** ... \n - **Fluxo Alternativo:** ...
    uc_blocks = re.split(r'### UC', artifact_content)
    for block in uc_blocks[1:]:
        uc_num = block[:2] # '01', '02', etc
        lines = block.split('\n')
        flows_text = ""
        for line in lines[1:]:
            if line.strip() and not line.startswith('---'):
                flows_text += line + "\n"
        flows_dict[uc_num] = flows_text.strip()

# Now inject them into the READMEs
if os.path.exists(astah_dir):
    for root, dirs, files in os.walk(astah_dir):
        if "README.md" in files:
            filepath = os.path.join(root, "README.md")
            # Extract UC number from folder name like UC01_Realizar_Login
            folder_name = os.path.basename(root)
            if folder_name.startswith("UC"):
                uc_num = folder_name[2:4]
                if uc_num in flows_dict:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if "## 🌊 Fluxos" not in content:
                        # Insert right before "## 🚀 Tutorial" or "> [!IMPORTANT]"
                        insert_point = "## 🚀 Tutorial Passo a Passo"
                        if "> [!IMPORTANT]" in content:
                            insert_point = "> [!IMPORTANT]"
                        
                        injection = f"## 🌊 Fluxos (Normal e Alternativo)\n{flows_dict[uc_num]}\n\n"
                        new_content = content.replace(insert_point, injection + insert_point)
                        
                        # Fix the mermaid class diagram to match private attributes
                        new_lines = []
                        for line in new_content.split('\n'):
                            if '+' in line and ':' in line and '(' not in line and '<<' not in line:
                                line = line.replace('+', '-', 1)
                            new_lines.append(line)
                        new_content = '\n'.join(new_lines)
                        
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Atualizado: {filepath} (Fluxos injetados e Mermaid atualizado)")

print("Script concluído com sucesso!")
