import os

# read original files and write cleaned version in new files

def remove_noise_info(content_list):
    for i in range(len(content_list)):
        if content_list[i].startswith(('<Sync','<Who','<Event')):
            content_list[i]=''
    return content_list

def write_new_files(cleaned_content_list, old_file_path, encoding='utf8'):
    with open(f"cleaned_{old_file_path.split('/')[-1]}",'w', encoding=encoding) as f:
            for content in cleaned_content_list:
                f.write(content)

def process_files_in_dir(dir, encoding):
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        with open(file_path,'r', encoding=encoding) as f:
            content = f.readlines()
            content_cleaned = remove_noise_info(content)
        write_new_files(content_cleaned, file_path, 'utf8')

if __name__ == "__main__":
    process_files_in_dir("/eslo_entretien", 'cp1252')
