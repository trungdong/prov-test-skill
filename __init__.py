from mycroft import MycroftSkill, intent_file_handler


class ProvTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.prov.intent')
    def handle_test_prov(self, message):
        self.speak_dialog('test.prov')


def create_skill():
    return ProvTest()

