import re
from .templates import ESTRUCTURA_CODE_OPEN, ESTRUCTURA_CODE_CLOSE

class MarkDownParser:
    def __init__(self):
        self.on_lista = False
        self.on_cita = False
        self.on_code = False
        self.on_tabla = False
        self.on_p = False
        self.lista_niveles = []

    def parse_line(self, line):
        indent = len(line) - len(line.lstrip())
        temp = line.strip()
        cierre = ""

        if self.on_code:
            if temp.startswith('```'):
                temp = ESTRUCTURA_CODE_CLOSE
                self.on_code = False
            else:
                temp = temp.replace('<', '&lt;').replace('>', '&gt;')
        else:
            match_ul = re.match(r'^(\s*)-\s+', line)
            match_ol = re.match(r'^(\s*)\d+\.\s+', line)
            is_lista_line = match_ul or match_ol
            is_structural = any(temp.startswith(x) for x in ['#', '>', '|', '---', '```']) or is_lista_line
            
            if self.on_p and (not temp or is_structural):
                cierre += "</p>"
                self.on_p = False

            if temp.startswith('```'):
                temp = ESTRUCTURA_CODE_OPEN
                self.on_code = True
            else:
                if self.on_lista and (not temp or (not is_lista_line and is_structural)):
                    if not is_lista_line:
                        while self.lista_niveles:
                            tag = self.lista_niveles.pop()['tag']
                            cierre += f"</li></{tag}>"
                        self.on_lista = False
                
                if self.on_cita and (not temp or is_structural):
                    cierre += "</blockquote>"
                    self.on_cita = False

                if self.on_tabla and (not temp or not temp.startswith('|')):
                    cierre += "</tbody></table>"
                    self.on_tabla = False
                    
                if temp.startswith('|'):
                    celdas = [c.strip() for c in temp.split('|') if c.strip()]
                    if not self.on_tabla:
                        self.on_tabla = True
                        temp = "<table><thead><tr>" + "".join([f"<th>{c}</th>" for c in celdas]) + "</tr></thead><tbody>"
                    elif all(set(c.strip()) <= {'-', ':', ' '} for c in temp.split('|') if c.strip()):
                        return ""
                    else:
                        temp = "<tr>" + "".join([f"<td>{c}</td>" for c in celdas]) + "</tr>"
                elif temp.startswith('---'):
                    temp = '<hr>'
                    

                if temp.startswith('######'):
                    temp = '<h6>' + temp.lstrip('#').strip() + '</h6>'
                elif temp.startswith('#####'):
                    temp = '<h5>' + temp.lstrip('#').strip() + '</h5>'
                elif temp.startswith('####'):
                    temp = '<h4>' + temp.lstrip('#').strip() + '</h4>'    
                elif temp.startswith('###'):
                    temp = "<h3>" + temp.lstrip('#').strip() + '</h3>'
                elif temp.startswith('##'):
                    temp = "<h2>" + temp.lstrip('#').strip() + '</h2>'
                elif temp.startswith('#'):
                    temp = "<h1>" + temp.lstrip('#').strip() + '</h1>'   
                elif is_lista_line:
                    m = match_ul if match_ul else match_ol
                    tag = "ul" if match_ul else "ol"
                    indent = len(m.group(1))
                    content = line.strip().split(' ', 1)[1]
                    
                    if not self.on_lista:
                        self.on_lista = True
                        self.lista_niveles = [{'indent': indent, 'tag': tag}]
                        temp = f"<{tag}><li>{content}"
                    else:
                        if indent > self.lista_niveles[-1]['indent']:
                            self.lista_niveles.append({'indent': indent, 'tag': tag})
                            temp = f"<{tag}><li>{content}"
                        elif indent < self.lista_niveles[-1]['indent']:
                            cierre_niveles = "</li>"
                            while len(self.lista_niveles) > 1 and indent < self.lista_niveles[-1]['indent']:
                                last_tag = self.lista_niveles.pop()['tag']
                                cierre_niveles += f"</{last_tag}></li>"
                            temp = cierre_niveles + f"<li>{content}"
                        else:
                            if tag != self.lista_niveles[-1]['tag']:
                                old_tag = self.lista_niveles.pop()['tag']
                                self.lista_niveles.append({'indent': indent, 'tag': tag})
                                temp = f"</{old_tag}><{tag}><li>{content}"
                            else:
                                temp = "</li><li>" + content
                elif temp.startswith('>'):
                    if not self.on_cita:
                        temp = '<blockquote>' + temp.lstrip('>').strip()
                        self.on_cita = True
                    else:
                        temp = temp.lstrip('>').strip() + "<br>"
                elif not temp:
                    temp = ""
                elif self.on_lista or self.on_cita:
                    temp = temp + "<br>"
                else:
                    if not self.on_p:
                        temp = "<p>" + temp
                        self.on_p = True
                
                temp = cierre + temp
                temp = re.sub(r'~~(.*?)~~', r'<s>\1</s>', temp)
                temp = re.sub(r'`(.*?)`', r'<code>\1</code>', temp)
                temp = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', temp)
                temp = re.sub(r'\*(.*?)\*', r'<i>\1</i>', temp)
                temp = re.sub(r'__(.*?)__', r'<strong>\1</strong>', temp)
                
                temp = re.sub(r'_(.*?)_', r'<i>\1</i>', temp)
                temp = re.sub(r'\==(.*?)==', r'<mark>\1</mark>', temp)
                temp = re.sub(r'\!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', temp)
                temp = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', temp)
                temp = re.sub(r'\[\^(.*?)\]', r'<sup>\1</sup>', temp)
                temp = re.sub(r'\[x(.*?)\]', r'<input type="checkbox" checked>\1</input>', temp)
                temp = re.sub(r'\[(.*?)\]', r'<input type="checkbox">\1</input>', temp)
                

        return temp
