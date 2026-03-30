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
    st.subheader("Your interactive interface for qualitative discourse analysis on defence and security communication.")

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
            "The app helps users engage with discourse analysis in an interactive way. "
            "It provides a space to navigate concepts, explore discourse material, "
            "and compare themes, cases, and communicative patterns."
        )

        st.markdown("### Why was it created?")
        st.write(
            "Aithra was developed as a bridge between qualitative research and digital "
            "research communication. It translates complex analytical work into a form "
            "that is easier to access and explore."
        )

        st.markdown("### Who is it for?")
        st.write(
            "The interface can be useful for researchers, students, and wider audiences "
            "interested in defence, security, discourse, and political communication."
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
            "The research focuses on defence and security communication in Europe. "
            "It examines how political and institutional actors communicate about "
            "security issues, justify strategic choices, and construct meaning around "
            "threat, responsibility, legitimacy, and defence."
        )

        st.markdown("### Research focus")
        st.write(
            "The project is interested in discourse as a way of understanding how defence "
            "and security are framed, explained, and made politically meaningful."
        )

        st.markdown("### Analytical perspective")
        st.write(
            "Using qualitative discourse analysis, the research explores recurring themes, "
            "narratives, and justificatory patterns in communication related to defence "
            "and security."
        )

        st.markdown("### Why does this matter?")
        st.write(
            "Public discourse shapes how security challenges are understood and how policy "
            "responses become legitimate. Studying these narratives helps reveal how defence "
            "and security are politically communicated."
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
        st.title("Historical development of the industrial-military complex")

        if st.button("← Back to Theory"):
            st.query_params["page"] = "Theory"
            st.query_params["theory"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "The industrial-military complex provides an important historical backdrop for understanding "
            "how defence institutions, political actors, and industrial interests became increasingly intertwined."
        )

        st.write(
            "Over time, defence communication evolved alongside these institutional and economic structures. "
            "This historical development shaped how military capacity, security needs, and strategic priorities "
            "were publicly framed and legitimised."
        )

        st.markdown("### Why this matters for Aithra")
        st.write(
            "Understanding this background helps situate contemporary defence discourse within longer histories "
            "of political communication, institutional authority, and public justification."
        )

    elif theory_page == "genz":
        st.title("Why Gen Z as a key audience")

        if st.button("← Back to Theory"):
            st.query_params["page"] = "Theory"
            st.query_params["theory"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "Gen Z represents an especially important audience in contemporary communication because it engages "
            "with politics, media, and institutions in ways that differ from earlier generations."
        )

        st.write(
            "Digital habits, platform cultures, expectations of transparency, and new forms of political awareness "
            "shape how younger audiences interpret institutional messages, including those related to defence and security."
        )

        st.markdown("### Why this matters for the project")
        st.write(
            "Focusing on Gen Z helps highlight how defence communication must adapt when addressing audiences that are "
            "digitally socialised, media-critical, and often distant from traditional strategic language."
        )

    elif theory_page == "cross_communication":
        st.title("Cross-communication challenges")

        if st.button("← Back to Theory"):
            st.query_params["page"] = "Theory"
            st.query_params["theory"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "Communicating defence and security issues is challenging because messages often move across very different "
            "audiences, institutional settings, and communicative expectations."
        )

        st.write(
            "What may appear clear and legitimate in one context can seem opaque, distant, or unconvincing in another. "
            "This creates tensions between expert language and public accessibility, between institutional priorities "
            "and audience reception, and between strategic messaging and democratic communication."
        )

        st.markdown("### Relevance for Aithra")
        st.write(
            "Aithra helps make these challenges more visible by creating a space in which discourse can be explored, "
            "compared, and interpreted across communicative settings."
        )

    elif theory_page == "discourse_theory":
        st.title("Discourse theory")

        if st.button("← Back to Theory"):
            st.query_params["page"] = "Theory"
            st.query_params["theory"] = "overview"
            st.rerun()

        st.markdown("---")

        st.write(
            "Discourse theory provides the conceptual basis for analysing how language produces meaning, structures "
            "interpretation, and shapes political reality."
        )

        st.write(
            "Rather than treating communication as neutral information transfer, discourse theory highlights how ideas, "
            "categories, and narratives are constructed, repeated, and made socially meaningful."
        )

        st.write(
            "In the context of defence and security, this means asking how threats, responsibilities, legitimacy, "
            "and strategic priorities are framed through language."
        )

        st.markdown("### Why discourse theory is central here")
        st.write(
            "Aithra is grounded in the idea that discourse does not simply reflect security politics — "
            "it actively helps constitute how security is understood and communicated."
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