# scripts/flatten_images.py
import os
import shutil
import re

def flatten():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    userflows_dir = os.path.join(base_dir, "Acconeer_ERP_UserFlows")
    target_images_dir = os.path.join(base_dir, "images")
    
    os.makedirs(target_images_dir, exist_ok=True)
    
    print(f"Base Directory: {base_dir}")
    print(f"Target Images Directory: {target_images_dir}")
    
    copied = 0
    mapping = {}
    
    if os.path.exists(userflows_dir):
        for root, dirs, files in os.walk(userflows_dir):
            for f in files:
                src_path = os.path.join(root, f)
                rel_userflows = os.path.relpath(src_path, base_dir).replace("\\", "/")
                dst_path = os.path.join(target_images_dir, f)
                
                shutil.copy2(src_path, dst_path)
                mapping[rel_userflows] = f"images/{f}"
                copied += 1
                
        print(f"Copied {copied} images from Acconeer_ERP_UserFlows to images/")
    else:
        print("Acconeer_ERP_UserFlows does not exist, checking images/")

    # Also copy logo files if they exist in base_dir
    for logo in ["spectrum-zestwings-logo.png", "spectrum_shield.png", "spectrum_zestwings_logo.png"]:
        logo_path = os.path.join(base_dir, logo)
        if os.path.exists(logo_path):
            shutil.copy2(logo_path, os.path.join(target_images_dir, logo))
            print(f"Copied {logo} to images/")

    # Update scripts: pages_p01_p08.py, pages_p09_p16.py, pages_p17_p26.py
    scripts_dir = os.path.join(base_dir, "scripts")
    script_files = ["pages_p01_p08.py", "pages_p09_p16.py", "pages_p17_p26.py", "generate_complete_manual.py"]
    
    for sf in script_files:
        sf_path = os.path.join(scripts_dir, sf)
        if not os.path.exists(sf_path):
            continue
        with open(sf_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace Acconeer_ERP_UserFlows/.../filename.png with images/filename.png
        new_content = re.sub(r"Acconeer_ERP_UserFlows/[^/\"\']+/([a-zA-Z0-9_\-\.]+\.(?:png|jpg|jpeg|svg))", r"images/\1", content)
        
        if new_content != content:
            with open(sf_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated image paths in {sf}")
        else:
            print(f"No image paths changed in {sf}")

    # Verify that all images referenced in scripts exist in images/
    all_refs = []
    for sf in script_files:
        sf_path = os.path.join(scripts_dir, sf)
        if not os.path.exists(sf_path):
            continue
        with open(sf_path, "r", encoding="utf-8") as f:
            matches = re.findall(r"images/([a-zA-Z0-9_\-\.]+\.(?:png|jpg|jpeg|svg))", f.read())
            all_refs.extend(matches)
            
    print(f"Total image references found: {len(all_refs)}")
    missing = [img for img in all_refs if not os.path.exists(os.path.join(target_images_dir, img))]
    if missing:
        print(f"WARNING: Missing images in {target_images_dir}: {missing}")
    else:
        print("ALL referenced images verified to exist in images/!")

    # Now remove the old Acconeer_ERP_UserFlows folder and its subfolders
    if os.path.exists(userflows_dir) and not missing:
        shutil.rmtree(userflows_dir)
        print("Successfully removed Acconeer_ERP_UserFlows and all subfolders!")

if __name__ == "__main__":
    flatten()
