"""Settings for the production app"""

SEEDING_METHODS = [
    ('direct_seeding', 'Semis direct'),
    ('bulbs', 'Bulbilles'),
    ('tray', 'Plaque'),
    ('outsourced', 'Fournisseur')
]

TRAY_TYPES  = [
    ('15', '15'),
    ('20', '20'),
    ('48', '48'),
    ('77', '77'),
    ('150', '15'),
    ('273', '273'),
]

HARVEST_UNITS = [
    ('kg', 'kg'),('bottes', 'bottes'), ('pièces', 'pièces')]

GRIDS = [
    ('1x1', '1x1'),
    ('1x2', '1x2'),
    ('2x2', '2x2'),
    ('3x3', '3x3'),
    ('4x4', '4x4'),
    ('6x6', '6x6'),
]

EVENTS = [
    ('planting', 'Plantation'),
    ('seeding', 'Semis'),
    ('first_harvest', 'Première récolte'),
    ('last_harvest', 'Dernière récolte'),
    ('termination', 'Abandon')
]

REASONS_FOR_TERMINATING = [
    ('bitten_by_frost', 'Gel'),
    ('went_to_seed', 'Montée en graine'),
    ('too_slow', 'Croissance trop lente'),
    ('bad_quality', 'Qualité insuffisante'),
    ('better_alternative', 'Sacrifié pour une autre'),
    ('bad_germination', 'Mauvaise germination'),
    ('eaten_by_pest', 'Ravageur'),
]