# Dictionary with chemicals and their multiple properties
chemical_properties = {
    'hydrogen': ['chemical element', 'colorless gas', 'highly flammable'],
    'oxygen': ['chemical element', 'supports combustion', 'colorless gas'],
    'carbon': ['chemical element', 'found in all living things', 'forms diamond and graphite'],
    'nitrogen': ['chemical element', 'colorless gas', 'makes up 78% of air'],
    'helium': ['chemical element', 'noble gas', 'lighter than air'],

    'blue': ['color-related', 'used in pH indicators', 'common dye'],
    'red': ['color-related', 'used in warning signs', 'may indicate acid-base reaction'],
    'green': ['color-related', 'used in chlorophyll and pigments'],
    'yellow': ['color-related', 'used in paints and dyes'],
    'purple': ['color-related', 'associated with potassium permanganate'],

    'hydrochloric acid': ['acid', 'strong', 'used in cleaning', 'corrosive'],
    'sulfuric acid': ['acid', 'very strong', 'used in car batteries'],
    'nitric acid': ['acid', 'used in explosives and fertilizers'],

    'sodium hydroxide': ['base', 'strong alkali', 'used in soap making'],
    'potassium hydroxide': ['base', 'used in alkaline batteries', 'strong alkali'],
    'ammonia': ['base', 'pungent smell', 'used in fertilizers']
}

# Get input from user
chemical = input("Enter the name of a chemical: ").strip().lower()

# Check and print properties
if chemical in chemical_properties:
    print(f"\nProperties of {chemical.title()}:")
    for prop in chemical_properties[chemical]:
        print(f"-> {prop}")
else:
    print(f"\nNo data found for '{chemical}'.")
