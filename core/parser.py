import re
from .templates import ESTRUCTURA_CODE_OPEN, ESTRUCTURA_CODE_CLOSE

class MarkDownParser:
    def __init__(self):
        self.on_lista = False
        self.on_cita = False
        self.on_code = False

    def parse_line(self, line):
        temp = line.strip()
        cierre = ""

        if self.on_code:
            if temp.startswith('```'):
                temp = ESTRUCTURA_CODE_CLOSE
                self.on_code = False
            else:
                temp = temp.replace('<', '&lt;').replace('>', '&gt;')
        else:
            if temp.startswith('```'):
                temp = ESTRUCTURA_CODE_OPEN
                self.on_code = True
            else:
                if self.on_lista and (not temp or temp.startswith('#') or temp.startswith('>')):
                    cierre += "</ul>"
                    self.on_lista = False
                    
                if temp.startswith('---'):
                    temp = '<hr>'
                    
                if self.on_cita and (not temp or temp.startswith('#') or temp.startswith('- ')):
                    cierre += "</blockquote>"
                    self.on_cita = False

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
                elif temp.startswith('- '):
                    if not self.on_lista:
                        temp = '<ul><li>' + temp.lstrip('- ').strip() + '</li>'
                        self.on_lista = True
                    else:
                        temp = '<li>' + temp.lstrip('- ').strip() + '</li>'
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
                
                temp = cierre + temp
                temp = re.sub(r'`(.*?)`', r'<code>\1</code>', temp)
                temp = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', temp)
                temp = re.sub(r'\*(.*?)\*', r'<i>\1</i>', temp)
                temp = re.sub(r'__(.*?)__', r'<strong>\1</strong>', temp)
                temp = re.sub(r'_(.*?)_', r'<i>\1</i>', temp)
                temp = re.sub(r'\==(.*?)==', r'<mark>\1</mark>', temp)
                temp = re.sub(r'\!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', temp)
                temp = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', temp)

        return temp
