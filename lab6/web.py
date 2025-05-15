from playhouse.shortcuts import model_to_dict
from lab6 import *
import cherrypy

class CallCenter:
    @cherrypy.expose
    def index(self):
        data_ent = Data.select()
        data_list = [model_to_dict(entry) for entry in data_ent]
        return self.render_index(data_list)

    @cherrypy.expose
    def stop(self):
        cherrypy.engine.exit()

    def render_index(self, data_list):
        html = '<html><head><title>Лабораторна работа №6</title></head><body>'
        html += '<h1>Данные call-центра</h1>'
        html += '<table border="1">'
        html += '<tr><th>ID</th><th>Номер телефона</th><th>Причина звонка</th><th>Получен ли ответ</th></tr>'

        for en in data_list:
            answer = "Неизвестно" if en["answer"] is None else ("Да" if bool(en["answer"]) else "Нет")
            html += f'<tr><td>{en["id"]}</td><td>{en["number"]}</td><td>{en["request"]}</td><td>{answer}</td></tr>'

        html += '</table>'
        html += '</body></html>'

        html += '''
            <h1>Добавить новую запись</h1>
            <form method="post" action="/add_submit">
                <label>Номер телефона:</label><br>
                <input type="text" name="number" required><br><br>
                <label>Причина звонка:</label><br>
                <input type="text" name="request" required><br><br>
                <label>Ответ получен:</label><br>
                <select name="answer">
                    <option value="true">Да</option>
                    <option value="false">Нет</option>
                </select><br><br>
                <input type="submit" value="Добавить">
            </form>
        '''

        html += '''
          <h1>Изменить запись</h1>
            <form method="post" action="/change_submit">
                <label>Id</label><br>
                <input type="number" name="id" required><br><br>
                <label>Номер телефона:</label><br>
                <input type="text" name="number" required><br><br>
                <label>Причина звонка:</label><br>
                <input type="text" name="request" required><br><br>
                <label>Ответ получен:</label><br>
                <select name="answer">
                    <option value="true">Да</option>
                    <option value="false">Нет</option>
                </select><br><br>
                <input type="submit" value="Изменить">
            </form>
        '''

        return html

    @cherrypy.expose
    def add_submit(self, number, request, answer):
        answer_value = True if answer == "true" else False
        Data.create(number=number, request=request, answer=answer_value)
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def change_submit(self, id, number, request, answer):
        record = Data.get(Data.id == int(id))
        record.number = number
        record.request = request
        record.answer = True if answer == "true" else False
        record.save()
        raise cherrypy.HTTPRedirect('/')

if __name__ == '__main__':
    cherrypy.quickstart(CallCenter(), '/')
