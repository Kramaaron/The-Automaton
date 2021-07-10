from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
import streamlit as strr
import base64

def render_svg(svg):
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    strr.write(html, unsafe_allow_html=True)

q1 = ["1: ( b + aa + ab ) ( a + b )* ( bb + aba + ab )* ( aaa + bbb ) ( a + b ) ( a + b + ab )*", "( b + aa + ab ) ( a + b )* ( bb + aba + ab )* ( aaa + bbb ) ( a + b ) ( a + b + ab )*"]
q2 = ["2: ( 1 + 0 )* (11 + 00 + 101 + 010) ( 1 + 0 + 11 + 00 + 101 )* ( 11 + 00 ) ( 11+ 00 + 101 )* ( 1 + 0 ) ( 1 + 0 + 11 )*", "( 1 + 0 )* (11 + 00 + 101 + 010) ( 1 + 0 + 11 + 00 + 101 )* ( 11 + 00 ) ( 11+ 00 + 101 )* ( 1 + 0 ) ( 1 + 0 + 11 )*"]

strr.set_page_config(page_title = "The Automaton", layout = "centered")
strr.write("<h1 style = 'text-align: center'>The Automaton</h1>", unsafe_allow_html = True)

strr.subheader('Select Expression:')
choice = strr.selectbox("", [q1[0], q2[0]])

if choice == q1[0]:
    strr.subheader('Regular Expression:')
    strr.write("<p style = 'text-align: center;'</p>" + q1[1], unsafe_allow_html = True)
    dfa = VisualDFA(
    states = {"-", "1", "2", "3", "4", "5", "6", "7", "+"},
    input_symbols = {"a", "b"},
    transitions = {
        "-" : {"a" : "1", "b" : "2"},
        "1" : {"a" : "2", "b" : "2"},
        "2" : {"a" : "3", "b" : "4"},
        "3" : {"a" : "5", "b" : "4"},
        "4" : {"a" : "3", "b" : "6"},
        "5" : {"a" : "7", "b" : "4"},
        "6" : {"a" : "3", "b" : "7"},
        "7" : {"a" : "+", "b" : "+"},
        "+" : {"a" : "+", "b" : "+"},
    },
    initial_state = "-",
    final_states = {"+"},
    )

if choice == q2[0]:
    strr.subheader('Regular Expression:')
    strr.write("<p style = 'text-align: center;'</p>" + q2[1], unsafe_allow_html = True)
    dfa = VisualDFA(
    states = {"-", "q1", "q2", "q3", "q4", "q5","q6","q7","q8","+"},
    input_symbols = {"0", "1"},
    transitions = {
        "-" : {"0" : "q3", "1" : "q1"},
        "q1" : {"0" : "q4", "1" : "q5"},
        "q2" : {"0" : "q5", "1" : "q5"},
        "q3" : {"0" : "q5", "1" : "q2"},
        "q4" : {"0" : "q5", "1" : "q5"},
        "q5" : {"0" : "q7", "1" : "q6"},
        "q6" : {"0" : "q7", "1" : "q8"},
        "q7" : {"0" : "q8", "1" : "q6"},
        "q8" : {"0" : "+", "1" : "+"},
        "+" : {"0" : "+", "1" : "+"},
    },
    initial_state = "-",
    final_states = {"+"},
    )

try:     

    graph = dfa.show_diagram() 

    with strr.form(key = 'my_form'):
        strr.header("String Checker")
        strr.subheader("Input Strings")
        inpt = strr.text_input("")
        check = strr.form_submit_button('Check')

        inpt = inpt.replace(" ", "")
        inpt = inpt.replace("\"", "")
            
        if not inpt:
            strr.info("Input a string.")

        elif check:
            try: 
                accept = dfa.input_check(inpt)
                if "[Accepted]" in accept:
                    out = "valid."
                    graph = dfa.show_diagram(inpt) 
                    strr.success("The String `" + inpt + "` is " + out)
                else: 
                    out = "invalid."
                    graph = dfa.show_diagram(inpt)
                    strr.error("The String `" + inpt + "` is " + out) 
            except:
                strr.error("The Input String is invalid!")
    
    strr.write("")

    graph.format = "svg"
    graph.render("Automatonoutput")
    f = open("Automatonoutput.svg")
    lines = f.readlines()
    line_string=''.join(lines) 
    strr.subheader("Deterministic Finite Automata:")
    render_svg(line_string)
    
except:
    strr.empty()

strr.write("")

if choice == q1[0]:
    strr.subheader('Context-Free Grammar:')
    strr.write("<p style = 'text-align: center;'</p>" + ''' 
                                    Start symbol: S \n
                                    S → ABCDEF  \n
                                    A → b | aa | ab \n
                                    B → aB | bB | λ \n
                                    C → bbC | abaC | abC | λ \n
                                    D → aaa | bbb \n
                                    E → a | b  \n		
                                    F → aF | bF | abF | λ \n
                                    ''', unsafe_allow_html = True)

if choice == q2[0]:
    strr.subheader('Context-Free Grammar:')
    strr.write("<p style = 'text-align: center;'</p>" + ''' 
                                    Start symbol: S \n
                                    S → ABCDEFG  \n
                                    A → 1A | 0A | λ \n
                                    B → 11 | 00 | 101 | 010 \n
                                    C → 1C | 0C | 11C | 00C | 101C \n
                                    D → 11 | 00 \n
                                    E → 11E | 00E | 101E | λ  \n		
                                    F → 1 | 0 \n
                                    G → 1G | 0G | 11G | λ \n
                                    ''', unsafe_allow_html = True)
