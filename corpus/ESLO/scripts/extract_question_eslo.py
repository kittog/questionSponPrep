import os
import re
import pandas as pd
import xml.etree.ElementTree as ET

# extract questions from cleaned corpus ==> list of tuples [(context_previous, question, context_next)] ==> dataframe ==> csv

def get_tags(file_path, tag):
    root = ET.parse(file_path).getroot()
    tags = [t for t in root.iter(tag)]
    return tags

def check_discourse_markers(text):
    discourse_markers = ['ah oui ?', 'ah bon ?', 'oui ?', 'hein ?']
    for marker in discourse_markers:
        if text == marker :
            return False
    return True

def get_previous_context(i, tags):
    context_p = ''
    for o in range(4, -1, -1):
        if tags[i-o-1] != '\n':
            speaker_p = '#' + tags[i-o-1].attrib['speaker'].strip('\n')
            context_p +=  (speaker_p + tags[i-o-1].text.strip('\n')+ ' | ')
    return context_p

def get_next_text(i, tags):
    context_n = ''
    for o in range(5):
        if tags[i+o+1] != '\n':
            speaker_n = '#' + tags[i+o+1].attrib['speaker'].strip('\n') + ' : '
            context_n += (speaker_n + tags[i+o+1].text.strip('\n') + ' | ')
    return context_n

def get_questions_with_contexts(dir):
    questions_with_contexts = []
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        tags = get_tags(file_path, 'Turn')
        try:
            for i in range(5, len(tags)-5):
                tag = tags[i]
                text = tag.text
                try:
                    for t in text.split('\n'):
                        if '?' in t and check_discourse_markers(t):
                            speaker = '#' + tag.attrib['speaker'] + ' : '
                            t = speaker + t
                            context_p = get_previous_context(i, tags)
                            context_n = get_next_text(i, tags)
                            questions_with_contexts.append((context_p, t, context_n))
                except:
                    pass
        except:
            pass
    return questions_with_contexts

def replace_crlf(text):
    text = re.sub(r"\n+", "\n", text)

if __name__ == "__main__":
    questions_with_contexts = get_questions_with_contexts('../cleaned_eslo_entretien')
    df = pd.DataFrame(questions_with_contexts, columns=['previous_5_turn', 'question', 'next_5_turn'])
    df.previous_5_turn = df.previous_5_turn.apply(replace_crlf)
    df.next_5_turn = df.next_5_turn.apply(replace_crlf)
    df.to_csv('eslo_entretien.csv', sep=';', encoding='utf8')