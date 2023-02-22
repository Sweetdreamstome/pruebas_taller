from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'group'
    form_fields = ['kept']

    def is_displayed(self):
        return self.player.id_in_group == 1


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    def before_next_page(self):
        self.player.pago = self.participant.vars['pagos'] #+ una variable que se crea en dictator 'pago'


class Results(Page):
    def vars_for_template(self):
        return dict(offer=Constants.endowment - self.group.kept)


page_sequence = [Introduction, Offer, ResultsWaitPage, Results]
