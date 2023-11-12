import transitions
from transitions import State
from transitions.extensions import GraphMachine
from transitions import Transition

class arcum_machine:
    
    class model:

        def __init__(self):
            pass



    def __init__(self, model : model):
        self.inital = State(name = "home_page")
        self.model = model
        self.graphic_model = arcum_machine.model()
        self.states = [
                self.inital,
                State(name = 'choose_summon' ),
                State(name = "click_party_ok"),
                State(name = "loading_page"),
                State(name = 'play_page'),
                State(name = 'goal_page'),
                ]
        self.transitons = [
                # example {'trigger' : "name", "source" : "start_state", 'dest' : 'dest_state',  conditons unless before after prepare}
                {   'trigger' : 'open_url',
                    'source' : "home_page",
                    'dest' : "choose_summon",
                    'after' : 'check_summon_page'
                    }, 
                {   'trigger' : 'click_summon',
                    'source' : 'choose_summon',
                    'dest' : 'click_party_ok',
                    },
                {
                    'trigger' : 'click_party_ok',
                    'source' : 'click_party_ok',
                    'dest' : 'play_page'
                    },
                {
                    'trigger' : 'play',
                    'source' : 'play_page',
                    'dest' : 'goal_page'
                    }
                #  {
#
#
                    #  }
                #  {
#
                    #  }
                ]
        self.machine = transitions.Machine(
                model = self.model,
                states = self.states,
                initial = self.inital
                )
        self.generate_png()
        pass


    def generate_png(self):
        machine = GraphMachine(
                model = self.graphic_model,
                states = self.states,
                transitions = self.transitons,
                show_auto_transitions = False,
                initial = self.inital
                )
        roi = machine.get_graph(show_roi=True).draw('my_state_diagram.png', prog='dot')

m = arcum_machine.model()
am = arcum_machine(m)
am.generate_png()

