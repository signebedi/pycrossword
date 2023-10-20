import json
from PIL import Image, ImageDraw, ImageFont
import puz

# Read JSON data from file
with open('data.json', 'r') as file:
    data = json.load(file)

p = puz.Puzzle()

# Define puzzle properties
p.title = 'Crossword Puzzle'
p.author = 'ChatGPT'
p.width, p.height = 21, 21
p.preamble = data["crossword"]["theme"]

# Add words to crossword
for entry in data["crossword"]["words"]:
    p.fill_word(entry["word"], entry["clue"])

# Save the crossword to a .puz file (optional, can be opened with Across Lite)
p.save('crossword.puz')

# Generate crossword image
def generate_crossword_image(puzzle, output_path):
    cell_size = 30
    width, height = puzzle.width * cell_size, puzzle.height * cell_size

    img = Image.new('RGB', (width, height), color = 'white')
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('arial.ttf', 15)

    for y in range(puzzle.height):
        for x in range(puzzle.width):
            if puzzle.solution[y][x] == '.':
                d.rectangle([x*cell_size, y*cell_size, (x+1)*cell_size, (y+1)*cell_size], fill='black')

    for number, clue in puzzle.clues:
        x, y, direction, answer = clue
        d.text((x*cell_size+5, y*cell_size+5), str(number), font=fnt, fill='black')

    img.save(output_path)

generate_crossword_image(p, 'crossword_image.png')
