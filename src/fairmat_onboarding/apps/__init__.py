from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Menu,
    MenuItemTerms,
    Rows,
    SearchQuantities,
)

SCHEMA = 'fairmat_onboarding.schema_packages.schema_package.PIOnboardingQuestionnaire'

# General information
Q_PI_NAME = f'data.pi_name#{SCHEMA}'
Q_FAIRMAT_AREAS = f'data.fairmat_area_terms.value#{SCHEMA}'
Q_INSTITUTIONS = f'data.institution_terms.value#{SCHEMA}'
Q_RELATED_PROJECTS = f'data.related_project_terms.value#{SCHEMA}'
Q_RDM_CONTACT_PERSON = f'data.RDM_contact_person#{SCHEMA}'

# Research Focus
Q_RESEARCH_TYPE = f'data.research_focus.research_type#{SCHEMA}'
Q_RESEARCH_TOPICS = f'data.research_focus.research_topic_terms.value#{SCHEMA}'
Q_MATERIAL_SYSTEMS = f'data.research_focus.material_system_terms.value#{SCHEMA}'
Q_RESEARCH_METHODS = f'data.research_focus.research_method_terms.value#{SCHEMA}'

# Research Data
Q_DATA_TYPE = f'data.research_data_management.research_data.data_type#{SCHEMA}'
Q_FILE_FORMAT = f'data.research_data_management.research_data.file_format_terms.value#{SCHEMA}'

# NOMAD Usage
Q_TRAINING_TOPICS = f'data.NOMAD_usage.training_topic_terms.value#{SCHEMA}'
Q_USING_NOMAD = f'data.NOMAD_usage.using_nomad#{SCHEMA}'
Q_NOMAD_SERVICES = f'data.NOMAD_usage.nomad_service_terms.value#{SCHEMA}'

# Admin
Q_INTERVIEW_STATUS = f'data.onboarding_administration.interview_status#{SCHEMA}'

# Column display paths (slice notation required for repeated subsection values)
C_FAIRMAT_AREAS = f'data.fairmat_area_terms[0:8].value#{SCHEMA}'
C_INSTITUTIONS = f'data.institution_terms[0:3].value#{SCHEMA}'

onboarding_app = App(
    label='FAIRmat PI Onboarding',
    path='fairmat-onboarding',
    category='FAIRmat',
    description='Search and filter FAIRmat PI onboarding questionnaires.',
    filters_locked={
        'section_defs.definition_qualified_name': [SCHEMA],
    },
    search_quantities=SearchQuantities(
        include=[
            Q_PI_NAME,
            Q_FAIRMAT_AREAS,
            Q_INSTITUTIONS,
            Q_RELATED_PROJECTS,
            Q_RDM_CONTACT_PERSON,
            Q_RESEARCH_TYPE,
            Q_RESEARCH_TOPICS,
            Q_MATERIAL_SYSTEMS,
            Q_RESEARCH_METHODS,
            Q_DATA_TYPE,
            Q_FILE_FORMAT,
            Q_TRAINING_TOPICS,
            Q_USING_NOMAD,
            Q_NOMAD_SERVICES,
            Q_INTERVIEW_STATUS,
            C_FAIRMAT_AREAS,
            C_INSTITUTIONS,
        ]
    ),
    columns=[
        Column(search_quantity=Q_PI_NAME, label='PI Name', selected=True),
        Column(
            search_quantity=Q_RDM_CONTACT_PERSON,
            label='Contact Person',
            selected=True,
        ),
        Column(search_quantity=C_FAIRMAT_AREAS, label='FAIRmat Area(s)', selected=True),
        Column(search_quantity=C_INSTITUTIONS, label='Institution(s)', selected=False),
        Column(
            search_quantity=Q_INTERVIEW_STATUS,
            label='Interview Status',
            selected=True,
        ),
    ],
    rows=Rows(),
    menu=Menu(
        title='Filters',
        items=[
            Menu(
                title='General information',
                items=[
                    MenuItemTerms(
                        search_quantity=Q_PI_NAME,
                        title='PI Name',
                        show_input=True,
                        options=20,
                    ),
                    MenuItemTerms(
                        search_quantity=Q_FAIRMAT_AREAS,
                        title='FAIRmat Area',
                        show_input=False,
                        options=10,
                    ),
                    MenuItemTerms(
                        search_quantity=Q_INSTITUTIONS,
                        title='Institution',
                        show_input=True,
                        options=20,
                    ),
                    MenuItemTerms(
                        search_quantity=Q_RELATED_PROJECTS,
                        title='Network Projects',
                        show_input=True,
                        options=20,
                    ),
                ],
            ),
            Menu(
                title='Research Focus',
                items=[
                    MenuItemTerms(
                        search_quantity=Q_RESEARCH_TYPE,
                        title='Approach',
                        show_input=False,
                        options=5,
                    ),
                    MenuItemTerms(
                        search_quantity=Q_RESEARCH_TOPICS,
                        title='Research Topic',
                        show_input=True,
                        options=20,
                    ),
                    MenuItemTerms(
                        search_quantity=Q_MATERIAL_SYSTEMS,
                        title='Material System',
                        show_input=True,
                        options=20,
                    ),
                    MenuItemTerms(
                        search_quantity=Q_RESEARCH_METHODS,
                        title='Methods and Techniques',
                        show_input=True,
                        options=20,
                    ),
                ],
            ),
            Menu(
                title='Research Data',
                items=[
                    MenuItemTerms(
                        search_quantity=Q_DATA_TYPE,
                        title='Data Type',
                        show_input=False,
                        options=10,
                    ),
                    MenuItemTerms(
                        search_quantity=Q_FILE_FORMAT,
                        title='File Format',
                        show_input=True,
                        options=20,
                    ),
                ],
            ),
            Menu(
                title='NOMAD Usage',
                items=[
                    MenuItemTerms(
                        search_quantity=Q_TRAINING_TOPICS,
                        title='Desired Training Topic',
                        show_input=False,
                        options=10,
                    ),
                    MenuItemTerms(
                        search_quantity=Q_USING_NOMAD,
                        title='Currently Using NOMAD',
                        show_input=False,
                        options=5,
                    ),
                    MenuItemTerms(
                        search_quantity=Q_NOMAD_SERVICES,
                        title='NOMAD Service Used',
                        show_input=False,
                        options=10,
                    ),
                ],
            ),
            Menu(
                title='Admin',
                items=[
                    MenuItemTerms(
                        search_quantity=Q_INTERVIEW_STATUS,
                        title='Interview Status',
                        show_input=False,
                        options=5,
                    ),
                ],
            ),
        ],
    ),
)

app_entry_point = AppEntryPoint(
    name='FAIRmatOnboardingApp',
    description='Search and filter FAIRmat PI onboarding questionnaires.',
    app=onboarding_app,
)
