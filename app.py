import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Defence Discourse", layout="wide", page_icon="🛡️")

# Layout styling
st.markdown("""
    <style>
    .block-container {
        padding-top: 3rem;
        padding-left: 5rem;
        padding-right: 1rem;
        max-width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# Clickable logo -> back to landing screen
st.markdown("""
    <a href="/?page=landing" target="_self" style="text-decoration: none;">
        <div class="logo-left" style="
            width: 90px; 
            height: 90px; 
            border-radius: 50%; 
            background-color: #1D3557; 
            display: flex; 
            align-items: center; 
            justify-content: center;
            font-size: 25px; 
            font-weight: bold;
            color: white;
            font-family: Georgia, serif;
            margin-bottom: 6px;
            cursor: pointer;">
            Aithra
        </div>
    </a>
""", unsafe_allow_html=True)

# Menu setup
menu_options = ["About", "Theory", "Discourse Analysis", "Visuals", "Guide"]
page = st.query_params.get("page", "landing")

# Safety for old / invalid query params
if page == "Home":
    page = "About"

if page not in menu_options and page != "landing":
    page = "landing"

selected = option_menu(
    menu_title=None,
    options=menu_options,
    icons=["info-circle", "book", "bar-chart", "image", "compass"],
    orientation="horizontal",
    default_index=0 if page == "landing" else menu_options.index(page),
    styles={
        "nav-link-selected": {"background-color": "#1D3557"},
        "container": {
            "padding": "0px",
            "background-color": "#f0f2f6",
            "border-radius": "10px",
            "width": "100%",
        },
        "menu-icon": {"display": "none"},
    }
)
st.query_params["page"] = selected  

# Keep page state in URL unless user is on landing screen
if page != "landing":
    st.query_params["page"] = selected

# Landing screen
if page == "landing":
    st.title("Welcome to Aithra")
    st.subheader("A professional platform for exploring how defence and security narratives are constructed, compared, and interpreted in the media across the UK, Germany, France, and Spain.")

# About screen
elif selected == "About":
    about_page = st.query_params.get("about", "overview")

    # ABOUT OVERVIEW
    if about_page == "overview":
        st.title("About")
        st.subheader("Learn more about Aithra and the research behind it.")

        st.markdown("### Explore:")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### What is Aithra?")
            st.write(
                "Learn what Aithra is, what the app does, and how it supports "
                "interactive qualitative discourse analysis."
            )
            if st.button("Open Aithra Overview", key="go_aithra"):
                st.query_params["page"] = "About"
                st.query_params["about"] = "aithra"
                st.rerun()

        with col2:
            st.markdown("#### What is the research about?")
            st.write(
                "Learn about the research context, analytical focus, and why "
                "defence and security communication matter."
            )
            if st.button("Open Research Overview", key="go_research"):
                st.query_params["page"] = "About"
                st.query_params["about"] = "research"
                st.rerun()

    # AITHRA PAGE
    elif about_page == "aithra":
        st.title("What is Aithra?")

        if st.button("← Back to About"):
            st.query_params["page"] = "About"
            st.query_params["about"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "Aithra is an interactive research interface designed to make qualitative "
            "discourse analysis more accessible, structured, and explorable."
        )

        st.info(
            "The purpose of Aithra is to make qualitative discourse research "
            "comparable, transparent, and easier to explore through an interactive interface."
        )

        st.markdown("### What does the app do?")
        st.write(
            "Aithra translates qualitative thesis research into a clear and structured digital format."
            "It helps users compare findings and better understand how communication narratives are"
            "constructed across different national contexts."
        )

        st.markdown("### Why was it created?")
        st.write(
            "Aithra was created to present qualitative research in a more professional, accessible,"
            "and engaging way."
            "It transforms complex analytical work into a digital format that makes findings"
            "easier to navigate, compare, and communicate."
        )

        st.markdown("### Who is it for?")
        st.write(
            "The platform was developed primarily for the communication department to provide clear and"
            "easy access to the main findings of the master’s thesis. It can also serve anyone interested" 
            "in defence, security, and media discourse"

        )

    # RESEARCH PAGE
    elif about_page == "research":
        st.title("What is the research about?")

        if st.button("← Back to About"):
            st.query_params["page"] = "About"
            st.query_params["about"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "This platform is based on the master’s thesis"
            ""Perspectives on Security and Defence among Young Europeans and in the Media:""
            "A Cross-National Discourse Analysis on Communication Challenges for the Defence Industry."
        )

        st.markdown("### Research focus")
        st.write(
            "Developed in the Sustainability and Communication Department, the thesis explores how"
            "media discourse constructs meanings around security and defence and how these"
            "constructions contribute to shaping social reality."
            
            "It also examines how young Europeans talk about these issues in qualitative interviews,"
            "making it possible to compare media narratives with Gen Z perspectives across countries."

        )

        st.markdown("### Analytical perspective")
        st.write(
            "The study uses qualitative discourse analysis to examine how language shapes meanings around"
            "security and defence. It identifies recurring argumentation patterns, topoi, and metaphors"
            "in media discourse and compares them across cases. These findings are then related to Gen Z" 
            "interview narratives to assess similarities and differences between media discourse and Gen Z's"
            "perspectives."

        )

        st.markdown("### Why does this matter?")
        st.write(
            "Media discourse plays an important role in shaping how security and defence are understood,"
            "and socially legitimized. By comparing these media narratives with Gen Z interview perspectives,"
            "the study makes it possible to see whether dominant public narratives are reproduced, or challenged"
            "by younger audiences."

        )
elif selected == "Theory":
    theory_page = st.query_params.get("theory", "overview")

    # THEORY OVERVIEW
    if theory_page == "overview":
        st.title("Theory")
        st.subheader(
            "Explore the theoretical foundations that shape Aithra’s analytical perspective."
        )

        st.write(
            "This section introduces key theoretical perspectives that inform the project. "
            "It helps situate the app within broader debates on defence communication, "
            "audience engagement, discourse, and meaning-making."
        )

        st.markdown("---")

        st.markdown("### Explanatory video")
        st.write(
            "A short explanatory video will be added here to introduce the communication complexity "
            "in which defence companies operate, including questions of legitimacy, public perception, "
            "audience diversity, and strategic messaging."
        )

        st.markdown("""
        <div style="
            background-color: #f0f2f6;
            border: 1px dashed #999;
            border-radius: 10px;
            padding: 30px;
            text-align: center;
            color: #555;
            margin-top: 10px;
            margin-bottom: 20px;
        ">
            <strong>Explanatory video placeholder</strong><br>
            A future video will introduce the communication complexity surrounding defence companies.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### Explore the theory section")

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        with col1:
            st.markdown("#### Historical development of the industrial-military complex")
            st.write(
                "Understand the broader historical context in which defence communication emerged and evolved."
            )
            if st.button("Open", key="theory_imc"):
                st.query_params["page"] = "Theory"
                st.query_params["theory"] = "industrial_military_complex"
                st.rerun()

        with col2:
            st.markdown("#### Why Gen Z as a key audience")
            st.write(
                "Explore why younger generations are a particularly important audience in contemporary defence communication."
            )
            if st.button("Open", key="theory_genz"):
                st.query_params["page"] = "Theory"
                st.query_params["theory"] = "genz"
                st.rerun()

        with col3:
            st.markdown("#### Cross-communication challenges")
            st.write(
                "Examine the difficulties of communicating defence and security issues across different audiences and contexts."
            )
            if st.button("Open", key="theory_cross"):
                st.query_params["page"] = "Theory"
                st.query_params["theory"] = "cross_communication"
                st.rerun()

        with col4:
            st.markdown("#### Discourse theory")
            st.write(
                "Learn about the theoretical lens used to study language, meaning, and the construction of security narratives."
            )
            if st.button("Open", key="theory_discourse"):
                st.query_params["page"] = "Theory"
                st.query_params["theory"] = "discourse_theory"
                st.rerun()

    elif theory_page == "industrial_military_complex":
        st.title("The industrial-military complex")

        if st.button("← Back to Theory"):
            st.query_params["page"] = "Theory"
            st.query_params["theory"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "The industrial-military complex provides an important historical backdrop for understanding "
            "how defence institutions, political actors, and industrial interests became increasingly intertwined."
            
            "The concept of the military-industrial complex helps explain the close relationship between political"
            "decision-makers, military institutions, and defence companies. First introduced by Dwight D. Eisenhower"
            "in 1961, it draws attention to the growing influence that can emerge when security policy, industrial "
            "interests, and military structures become closely interconnected."
            
            "In the European context, this relationship is shaped by three overlapping levels, including the EU, "
            "national governments, and NATO. Together, these actors influence defence spending, industrial policy,"
            "strategic priorities, and the broader environment in which defence companies operate."
        )


        st.markdown("### Historical development of the industrial-military complex")
        st.write(
            "The European military-industrial complex developed in three main phases."
            "During the Cold War, defence production was largely state-driven and organised around national security"
            "priorities." 
            "After the Cold War, lower defence budgets, rising costs, and market pressures led to consolidation,"
            "privatisation, and greater European cooperation."
            "Since Russia’s invasion of Ukraine, defence has regained strategic urgency, bringing renewed investment,"
            "rearmament debates, and greater public visibility for defence companies."
            
            "Across these phases, defence companies have remained closely connected to governments, even as their role"
            "has become more corporate and internationally networked. This helps explain why the sector remains politically"
            "sensitive and why communication is closely tied to issues of legitimacy, sovereignty, and public acceptance."
        )
        
        
        st.markdown("### Why this matters?")
        st.info(
            "Understanding the historical background of the European military-industrial complex helps explain how current defence"
            "communication is shaped by questions of authority, legitimacy, and public acceptance. And it also helps understand the"
            "communication challenges that shape the sector today."

        )

    elif theory_page == "genz":
        st.title("Why Gen Z as a key audience")

        if st.button("← Back to Theory"):
            st.query_params["page"] = "Theory"
            st.query_params["theory"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "Generation Z is a key audience because it is the youngest generation entering adulthood and will play an increasingly"
            "important role in shaping Europe’s social, political, and economic future. Shaped by digital media, economic uncertainty,"
            "climate anxiety, and geopolitical crises, Gen Z approaches institutions, public issues, and communication differently from"
            "older generations."
            
            "These experiences influence how young people consume information, evaluate legitimacy, and form opinions on security and "
            "defence. At the same time, Gen Z is becoming more important as a workforce, an electorate, and a consumer group, which makes"
            "their attitudes especially relevant for organisations seeking long-term legitimacy and public relevance."
            
            "For the defence industry, this is particularly important because Gen Z often recognises the importance of security, while at"
            "the same time showing limited familiarity with defence companies and expressing ethical concerns about the sector. This makes"
            "Gen Z a strategically important audience for communication that aims to be credible, transparent, and socially meaningful."
        )

        st.write(
            "Digital habits, platform cultures, expectations of transparency, and new forms of political awareness "
            "shape how younger audiences interpret institutional messages, including those related to defence and security."
        )

        st.markdown("### Why this matters for the project")
        st.write(
            "Focusing on Gen Z helps explain why defence communication must respond to audiences that are digitally shaped,"
            "value-driven, and often distant from traditional defence narratives."

    elif theory_page == "cross_communication":
        st.title("Cross-communication challenges")

        if st.button("← Back to Theory"):
            st.query_params["page"] = "Theory"
            st.query_params["theory"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "Communicating in the defence sector is especially challenging for multinational companies operating across"
            "different national, linguistic, and political contexts. Messages need to remain strategically consistent at"
            "the corporate level while also being adapted to local expectations, public debates, and cultural norms."
            
            "What is clear, legitimate, or credible in one country may be interpreted differently in another. This creates"
            "tensions between global coordination and local adaptation, between expert language and public accessibility, "
            "and between corporate objectives and broader societal expectations."
        )


        st.markdown("### Relevance for Aithra")
        st.write(
            "Aithra helps make these challenges more visible by showing how defence and security narratives differ across"
            "national contexts. In this way, the platform supports a better understanding of how communication must be in" 
            "terpreted, adapted, and strategically managed across countries."
        )

    elif theory_page == "discourse_theory":
        st.title("Discourse theory")

        if st.button("← Back to Theory"):
            st.query_params["page"] = "Theory"
            st.query_params["theory"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "Discourse theory provides the conceptual foundation for analysing how language shapes meaning, structures " 
            "interpretation, and contributes to the construction of social reality. Rather than treating communication as"
            "neutral information transfer, it highlights how meanings, narratives, and categories are socially produced, " 
            "circulated, and made relevant through discourse."
        )

        st.write(
            "In the context of defence and security, this means examining how issues such as threat, responsibility, " 
            "legitimacy, and strategic priorities are constructed through media discourse. It also means understanding" 
            "discourse not only as individual texts, but as broader patterns of meaning shaped by social, institutional, " 
            "and historical contexts."
        )

        st.markdown("### Why discourse theory is central here")
        st.write(
            "Aithra is grounded in the idea that discourse does not simply reflect security politics,"
            "it actively helps constitute how security is understood, communicated, and legitimized."
        )





# Discourse Analysis screen
elif selected == "Discourse Analysis":
    analysis_page = st.query_params.get("analysis", "overview")

    # OVERVIEW
    if analysis_page == "overview":
        st.title("Discourse Analysis")
        st.subheader(
            "Explore the analytical approach, key findings, and cross-country comparison."
        )

        st.write(
            "This section presents how the discourse analysis was conducted, "
            "summarises the main findings, and allows users to compare selected countries."
        )

        st.markdown("---")
        st.markdown("### Explore the discourse analysis section")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("#### Analytical Approach")
            st.write(
                "Learn how the discourse analysis was conducted and how the material was examined."
            )
            if st.button("Open", key="analysis_approach"):
                st.query_params["page"] = "Discourse Analysis"
                st.query_params["analysis"] = "approach"
                st.rerun()

        with col2:
            st.markdown("#### Analysis Summary")
            st.write(
                "Read a concise overview of the most important findings and recurring patterns."
            )
            if st.button("Open", key="analysis_summary"):
                st.query_params["page"] = "Discourse Analysis"
                st.query_params["analysis"] = "summary"
                st.rerun()

        with col3:
            st.markdown("#### Compare Countries")
            st.write(
                "Compare the discourse analysis across the selected country cases."
            )
            if st.button("Open", key="analysis_compare"):
                st.query_params["page"] = "Discourse Analysis"
                st.query_params["analysis"] = "compare"
                st.rerun()

    # ANALYTICAL APPROACH
    elif analysis_page == "approach":
        st.title("Analytical Approach")

        if st.button("← Back to Discourse Analysis"):
            st.query_params["page"] = "Discourse Analysis"
            st.query_params["analysis"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "This project uses qualitative discourse analysis to examine how defence and security "
            "issues are communicated, framed, and justified across different national contexts."
        )

        st.write(
            "The analysis focuses on recurring themes, patterns of meaning-making, and the ways "
            "in which language constructs ideas such as threat, legitimacy, responsibility, and strategy."
        )

        st.markdown("### How the analysis was conducted")
        st.write(
            "The material was examined through close reading and thematic interpretation. "
            "Particular attention was given to recurring narratives, key concepts, justificatory language, "
            "and differences in communicative emphasis across cases."
        )

        st.markdown("### Analytical focus")
        st.markdown("""
        - framing of defence and security issues  
        - construction of threat and responsibility  
        - patterns of legitimacy and justification  
        - recurring narratives across country cases  
        - similarities and differences in discourse  
        """)

    # ANALYSIS SUMMARY
    elif analysis_page == "summary":
        st.title("Analysis Summary")

        if st.button("← Back to Discourse Analysis"):
            st.query_params["page"] = "Discourse Analysis"
            st.query_params["analysis"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "The discourse analysis reveals both shared and divergent patterns in how defence "
            "and security are communicated across the selected country cases."
        )

        st.markdown("### Key observations")
        st.markdown("""
        - defence communication often combines strategic justification with public legitimacy claims  
        - narratives of threat and responsibility appear across multiple contexts  
        - countries differ in tone, emphasis, and communicative style  
        - some cases place stronger emphasis on national security, while others stress cooperation or public trust  
        """)

        st.markdown("### Overall interpretation")
        st.write(
            "Taken together, the findings suggest that defence discourse is shaped not only by strategic concerns, "
            "but also by the need to communicate across diverse publics, political cultures, and institutional settings."
        )

    # COUNTRY COMPARISON
    elif analysis_page == "compare":
        st.title("Compare Countries")

        if st.button("← Back to Discourse Analysis"):
            st.query_params["page"] = "Discourse Analysis"
            st.query_params["analysis"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "Select one or more countries to compare how defence and security discourse is framed across cases."
        )

        countries = ["UK", "France", "Germany", "Spain"]

        selected_countries = st.multiselect(
            "Select countries",
            options=countries,
            default=countries
        )

        st.markdown("---")

        if selected_countries:
            comparison_data = {
                "UK": {
                    "Main focus": "Strategic credibility and international responsibility",
                    "Discursive emphasis": "Security leadership, defence readiness, alliance role",
                    "Tone": "Strategic and assertive"
                },
                "France": {
                    "Main focus": "Strategic autonomy and national defence capacity",
                    "Discursive emphasis": "Sovereignty, military capability, independent action",
                    "Tone": "State-centred and strategic"
                },
                "Germany": {
                    "Main focus": "Responsibility, legitimacy, and political caution",
                    "Discursive emphasis": "Public justification, democratic accountability, strategic adaptation",
                    "Tone": "Careful and legitimising"
                },
                "Spain": {
                    "Main focus": "Cooperation, stability, and institutional alignment",
                    "Discursive emphasis": "Collective security, partnership, European and international frameworks",
                    "Tone": "Cooperative and institutionally oriented"
                }
            }

            for country in selected_countries:
                st.markdown(f"## {country}")
                st.write(f"**Main focus:** {comparison_data[country]['Main focus']}")
                st.write(f"**Discursive emphasis:** {comparison_data[country]['Discursive emphasis']}")
                st.write(f"**Tone:** {comparison_data[country]['Tone']}")
                st.markdown("---")
        else:
            st.warning("Please select at least one country to display the comparison.")














# Visuals screen
elif selected == "Visuals":
    st.title("Visuals")
    st.write("This is the Visuals screen.")

# Guide screen
elif selected == "Guide":
    guide_page = st.query_params.get("guide", "overview")

    # GUIDE OVERVIEW
    if guide_page == "overview":
        st.title("Guide")
        st.subheader("Learn how to navigate and use Aithra.")

        st.markdown("### Explore the guide")
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        with col1:
            st.markdown("#### How to use Aithra")
            st.write(
                "Get a simple introduction to how users can move through the platform."
            )
            if st.button("Open", key="guide_use"):
                st.query_params["page"] = "Guide"
                st.query_params["guide"] = "use"
                st.rerun()

        with col2:
            st.markdown("#### What each screen does")
            st.write(
                "Understand the purpose of each section of the app."
            )
            if st.button("Open", key="guide_screens"):
                st.query_params["page"] = "Guide"
                st.query_params["guide"] = "screens"
                st.rerun()

        with col3:
            st.markdown("#### How to work with the material")
            st.write(
                "See how the app supports exploration of discourse material and themes."
            )
            if st.button("Open", key="guide_material"):
                st.query_params["page"] = "Guide"
                st.query_params["guide"] = "material"
                st.rerun()

        with col4:
            st.markdown("#### MVP limitations")
            st.write(
                "Read about the current scope and limitations of the prototype."
            )
            if st.button("Open", key="guide_limits"):
                st.query_params["page"] = "Guide"
                st.query_params["guide"] = "limitations"
                st.rerun()

    # HOW TO USE
    elif guide_page == "use":
        st.title("How to use Aithra")

        if st.button("← Back to Guide"):
            st.query_params["page"] = "Guide"
            st.query_params["guide"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "Aithra is designed as an interactive interface that helps users explore "
            "qualitative discourse analysis in a structured way."
        )

        st.markdown("### Suggested path")
        st.markdown("""
        1. Start with **About** to understand the purpose of the app and the research context.  
        2. Move to **Theory** to learn about the conceptual foundations of the analysis.  
        3. Use **Discourse Analysis** to explore qualitative material, themes, and discursive patterns.  
        4. Visit **Visuals** to view selected findings in a more accessible and comparative format.  
        5. Return to **Guide** whenever you need help navigating the platform.  
        """)

        st.info(
            "Aithra is intended to support exploration, orientation, and research communication."
        )

    # WHAT EACH SCREEN DOES
    elif guide_page == "screens":
        st.title("What each screen does")

        if st.button("← Back to Guide"):
            st.query_params["page"] = "Guide"
            st.query_params["guide"] = "overview"
            st.rerun()

        st.markdown("---")

        st.markdown("### About")
        st.write(
            "Introduces Aithra and explains the research background of the project."
        )

        st.markdown("### Theory")
        st.write(
            "Presents the conceptual and analytical foundations used in the discourse analysis."
        )

        st.markdown("### Discourse Analysis")
        st.write(
            "Provides access to qualitative material, themes, and examples of discourse analysis."
        )

        st.markdown("### Visuals")
        st.write(
            "Displays selected results, patterns, or comparisons in visual form."
        )

        st.markdown("### Guide")
        st.write(
            "Helps users understand how to navigate the platform and what to expect from the MVP."
        )

    # HOW TO WORK WITH THE MATERIAL
    elif guide_page == "material":
        st.title("How to work with the material")

        if st.button("← Back to Guide"):
            st.query_params["page"] = "Guide"
            st.query_params["guide"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "The platform is designed to help users engage with qualitative discourse material "
            "in a more structured and accessible way."
        )

        st.markdown("### What users can do")
        st.markdown("""
        - explore selected discourse excerpts  
        - identify recurring themes and concepts  
        - compare communicative patterns across cases  
        - connect theoretical ideas with empirical examples  
        - use visuals to support interpretation  
        """)

        st.write(
            "The focus is not on automated interpretation, but on supporting a guided exploration "
            "of discourse and meaning-making."
        )

    # LIMITATIONS
    elif guide_page == "limitations":
        st.title("Limitations")

        if st.button("← Back to Guide"):
            st.query_params["page"] = "Guide"
            st.query_params["guide"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "Aithra is currently presented as a minimum viable product. "
            "This means that some functions, content areas, and design features are still in development."
        )

        st.markdown("### Current limitations")
        st.markdown("""
        - the platform may include placeholder content  
        - some sections may still be under construction  
        - data coverage may be selective rather than complete  
        - analytical depth and interactivity will expand over time  
        """)

        st.warning(
            "This platform is intended as an exploratory and communicative prototype rather than a final full-featured platform."
        )
