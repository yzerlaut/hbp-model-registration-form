from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parent))
from kg_interaction import check_if_alias_is_already_taken

import requests
import json
import time, os

def filename_with_datetime(filename, folder='./', extension=''):
    return os.path.join(folder,  filename+'__'+time.strftime("%Y_%m_%d-%H:%M:%S")+extension)

def check_url_validity(url):
    """ imlemented in the request module """
    return requests.get(url).ok
    
class Registration_Form:
    
    def __init__(self):
        self.Widget_List = {}
        self.valid_url = False
        self.order = ['name', 'alias', 'contact', 'institution', 'contributors', 'description',
                      'fig_url', 'fig_display', 'species', 'region', 'cell_type', 'scope', 'abstraction',
                      'license', 'version_text', 'version_name', 'data_url', 'commit_id',
                      'version_description', 'version_parameter', 'submit']

            
        self.Widget_List['name'] = interactive(self.f,
                                              x=widgets.Text(\
                                                    value='',
                                                    placeholder='e.g. Layer V Network in CA1',
                                                    description='Name:',
                                                             layout={'width':'70%'}));
        self.Widget_List['alias'] = interactive(self.f_alias, {'manual': True, 'manual_name':'Check validity'},
                                              x=widgets.Text(\
                                                    value='',
                                                    placeholder='e.g. L5-CA1_Ntwk',
                                                    description='Alias:',
                                                             layout={'width':'70%'}));
        self.Widget_List['contact'] = interactive(self.f,
                                                    x=widgets.Text(\
                                                    value='',
                                                    placeholder='e.g. Smith, John D.',
                                                    description='Contact:',
                                                                   layout={'width':'70%'}));
        
        self.Widget_List['institution'] = interactive(self.f,
                                                    x=widgets.Text(\
                                                    value='',
                                                    placeholder='e.g. CNRS, France',
                                                    description='Institution:',
                                                                   layout={'width':'70%'}));
        
        self.Widget_List['contributors'] = interactive(self.f,
                                                    x=widgets.Text(\
                                                    value='',
                                                    description_tooltip='e.g. Smith, John D.; Dupont, Jean Paul; Mueller, Jan; Russo, Giovanni',
                                                    placeholder='e.g. Smith, John D.; Dupont, Jean Paul; Mueller, Jan; Russo, Giovanni',
                                                    description='Contributors:',
                                                                   layout={'width':'70%'}));
        
        self.Widget_List['description'] = interactive(self.f,
                                                        x=widgets.Textarea(
                                                        placeholder='Decribe the model here',
                                                        description='Description:',
                                                            layout={'width':'70%', 'height':'150px'}))
        # optional figure upload
        self.Widget_List['fig_url'] = interactive(self.f_fig,
                                                {'manual': True, 'manual_name':'Upload figure'},
                                                  x=widgets.Text(\
                                                    value='',
                                                    placeholder='e.g. https://raw.github.com/name/repo/branch/fig.png',
                                                    description='Fig. URL:',
                                                                 layout={'width':'70%'}));
        self.Widget_List['fig_display'] = widgets.Image(format='png',
                                                        width=50)
        
        self.Widget_List['species'] = interactive(self.f,
                                                        x=widgets.Dropdown(
                                                        options=['',
                                                                 'Callithrix Jacchus',
                                                                 'Homo Sapiens',
                                                                 'Macaca Mulata',
                                                                 'Monodelphis Domestica'
                                                                 'Rattus Norvegicus',
                                                                 'Rodentia',
                                                                 'Mus Musculus',
                                                                 'Other'],
                                                        value='',
                                                        description='Species:',
                                                            layout={'width':'70%'}))
                                                  
        self.Widget_List['region'] = interactive(self.f,
                                                        x=widgets.Dropdown(
                                                        options=['',
                                                                 'Cortex',
                                                                 'Hippocampus',
                                                                 'Cerebellum',
                                                                 'Other'],
                                                        value='',
                                                        description='Region:',
                                                            layout={'width':'70%'}))
        
        # self.Widget_List['cell_type'] = interactive(self.f,
        #                                                 x=widgets.Dropdown(
        #                                                 options=['', 
        #                                                          'Pyramidal Cell',
        #                                                          'Interneuron'],
        #                                                 value='',
        #                                                 description='Cell type:'))
 
        self.Widget_List['cell_type'] = interactive(self.f,
                                                        x=widgets.Text(
                                                            placeholder='e.g. L5 Pyramidal Cell',
                                                            description='Cell type::',
                                                            layout={'width':'70%'}))
        
        self.Widget_List['scope'] = interactive(self.f,
                                                        x=widgets.Dropdown(
                                                        options=['', 
                                                                 'network',
                                                                 'network: whole brain',
                                                                 'network: brain region',
                                                                 'network: microcircuit',
                                                                 'single cell',
                                                                 'subcellular',
                                                                 'subcellular: ion channel',
                                                                 'subcellular: molecular',
                                                                 'subcellular: signaling',
                                                                 'subcellular: spine',
                                                                 'Other'],
                                                        value='',
                                                        description='Model scope:',
                                                            layout={'width':'70%'}))

        self.Widget_List['abstraction'] = interactive(self.f,
                                                        x=widgets.Dropdown(
                                                        options=['', 
                                                                 'biophysical model',
                                                                 'cognitive model',
                                                                 'population model: neural field',
                                                                 'population model: neural mass',
                                                                 'protein structure',
                                                                 'protein structure',
                                                                 'rate neuron',
                                                                 'spiking neuron',
                                                                 'spiking neuron: integrate and fire',
                                                                 'systems biology: continuous',
                                                                 'systems biology: discrete',
                                                                 'systems biology: flux balance',
                                                                 'systems biology',
                                                                 'Other'],
                                                        value='',
                                                        description='Abstraction level:',
                                                            layout={'width':'70%'}))
        

        self.Widget_List['license'] = interactive(self.f,
                                                    x=widgets.RadioButtons(
                                                    options=['Free', 'OpenSource', 'CreativeCommons'],
                                                    description='License'))
 
        self.Widget_List['version_text'] = interactive(self.f,
                                                    x=widgets.HTML(placeholder='',
                                                        value="<b>Add a Version </b> (optional)",
                                                            layout={'width':'70%'}))
        self.Widget_List['version_name'] = interactive(self.f,
                                              x=widgets.Text(\
                                                    value='',
                                                    placeholder='e.g. v1.0',
                                                    description='Name:',
                                                    layout={'width':'70%'}));
        self.Widget_List['data_url'] = interactive(self.f_url,
                                                {'manual': True, 'manual_name':'Check data availability'},
                                                  x=widgets.Text(\
                                                    value='',
                                                    placeholder='e.g. https://github.com/name/repo',
                                                    description='URL location:'));
        self.Widget_List['commit_id'] = interactive(self.f_commit,
                                                {'manual': True, 'manual_name':'Check commit'},
                                                  x=widgets.Text(\
                                                    value='',
                                            placeholder='If using version control, please provide a commit ID: e.g. 8e4g23j',
                                              description='Commit:',
                                                                 layout={'width':'70%'}));
        self.Widget_List['version_description'] = interactive(self.f,
                                                        x=widgets.Textarea(
                                                        placeholder='Decribe the version',
                                                        description='Description:',
                                                            layout={'width':'70%', 'height':'150px'}))
        self.Widget_List['version_parameter'] = interactive(self.f,
                                                        x=widgets.Textarea(
                                                            placeholder='Specific parameters describing this version ?\ne.g. Vrest=-70mV, T=27deg,...',
                                                        description='Parameters:',
                                                            layout={'width':'70%', 'height':'150px'}))

        self.Widget_List['submit'] = interactive(self.f_submission,
                                                        x=widgets.ToggleButton(
                                                            value=False,
                                                            description=' * -> Submit <- * ',
                                                            disabled=False,
                                                            button_style='',
                                                            # tooltip='Description',
                                                            icon='check',
                                                            layout={'width':'70%', 'height':'50px'}))
        
    def f(self, x):
            return x
        
    def f_alias(self, x):
        check_if_alias_is_already_taken(x)
        return x

    def f_url(self, x):
        """
        checking url validity
        based on the implementation of the request module 
        """
        if len(x.split('http'))>1:
            if requests.get(x).ok:
                print('"%s" is a valid url' % x)
                self.valid_url = True
            else:
                print('"%s" does not seem to be a valid url, please check it' % x)
        else:
            print('please provide the full url: e.g. http://mysite.org/myfolder')
            
        return x
    
    def f_commit(self, x):

        if self.valid_url:
            baseline_url = self.Widget_List['data_url'].children[0].value
            new_url = baseline_url+'/archive/'+str(x)+'.zip'
            r = requests.get(new_url)
            if r.ok:
                print('downloading archive [...] \n ->', new_url)
                open('archive.zip', 'wb').write(r.content)
                print('done !')
            else:
                print('"%s" is not a valid commit, please modify it' % x)
        else:
            print('Please provide a valid "URL location" before')
        return x

    def f_fig(self, x):
        """
        downloading the image and displaying it in a widget
        """

        if len(x.split('http'))>1:
            r = requests.get(self.Widget_List['fig_url'].children[0].value)
            if r.ok:
                open('graphical_abstract.png', 'wb').write(r.content)
                self.Widget_List['fig_display'].value = open("graphical_abstract.png", "rb").read()
                self.Widget_List['fig_display'].width = 300
            else:
                print('"%s" does not seem to be a valid url, please check it' % x)
        else:
            print('please provide the full url: e.g. http://mysite.org/myfolder')
            
                
    def build_dictionary(self):
        dictionary = {}
        for key in self.order:
            if key not in ['submit', 'fig_display']:
                dictionary[key] = self.Widget_List[key].children[0].value
        return dictionary

    def f_submission(self, x):
        dictionary = self.build_dictionary()
        alias = str(dictionary['alias'])
        if x:
            if not alias=='':
                fn = filename_with_datetime(alias, folder='./', extension='.JSON')
                with open(fn, 'w') as f:
                    json.dump(dictionary, f)
                if os.path.isfile(fn):
                    print('Submission details succesfully saved')
                else:
                    print('Problem in saving the submission')
            else:
                print('Please complete the form')

    
    def fill_with_dictionary(self, dictionary):
        for key, val in dictionary.items():
            if key in self.Widget_List:
                self.Widget_List[key].children[0].value = val
            else:
                print('key "%s" is not present in the Registration Form' % key)

    def show_registration_form(self):
        print('-----------------------------------------------')
        print('--- MODEL REGISTRATION IN HBP MODEL CATALOG ---')
        print('-----------------------------------------------')
        for key in self.order:
            display(self.Widget_List[key])

    def close_widgets(self):
        for key, val in self.Widget_List.items():
            val.close()

    def print_registration_results(self):
        dict_string = ' {'
        for key in self.order:
            try:
                dict_string += '"%s":"%s",\n' % (key, self.Widget_List[key].children[0].value.replace("'","").replace('"',''))
            except AttributeError:
                pass
        dict_string += '}'
        print(dict_string)



