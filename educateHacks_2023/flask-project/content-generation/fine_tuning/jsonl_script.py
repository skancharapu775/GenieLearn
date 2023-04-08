import csv

'''
pip install --upgrade openai
export OPENAI_API_KEY = Key
openai tools fine_tunes.prepare_data -f tuning_data.csv


'''

data = [
    ['prompt', 'completion'],
    ['American Revolution, 2|', ' Boston Tea Party : A political protest that occurred in 1773, in which American colonists, frustrated and angry at Britain for imposing taxation without representation // Battle of Bunker Hill : A battle fought on June 17, 1775, during the Siege of Boston in the early stages of the American Revolutionary War. Although the British won the battle, it was a moral victory for the American forces and demonstrated that they could stand||'],
    ['Spanish Vocab, 2|', ' Hola : Hello // Adios : Goodbye||'],
    ['Spanish Food Vocab, 4|', ' El Jamon : A type of cured ham that is a staple in Spanish Cuisine // El chorizo : A spicy sausage commonly used in spanish dishes // El arroz : rice // la leche : milk||'],
    ['Hyperbolas, 3|', ' Asymptotes : A hyperbola has two asymptotes that intersect at the center and are perpendicular to the transverse axis. // the two points on the axis of hyperbola and are equidistant from the center of the hyperbola // The point where the axis of the hyperbola cuts the hyperbola||']
]

with open('tuning_data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write multiple rows
    writer.writerows(data)