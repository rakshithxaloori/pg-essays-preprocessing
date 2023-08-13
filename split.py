import os

output_dir = "split_essays"

for essay_filename in os.listdir("essays"):
    # Create an output directory if it doesn't exist
    if os.path.exists(os.path.join(output_dir, essay_filename)):
        # Delete all files in the directory
        for file in os.listdir(os.path.join(output_dir, essay_filename)):
            os.remove(os.path.join(output_dir, essay_filename, file))
        # Delete the directory
        os.rmdir(os.path.join(output_dir, essay_filename))

    # Create the directory
    os.makedirs(os.path.join(output_dir, essay_filename))

    # Read the essay file
    audio_split = []
    with open(os.path.join("essays", essay_filename), "r") as essay_file:
        essay = essay_file.read()
        # Split the essay into at newlines
        paragraphs = essay.split("\n")
        # Remove empty paragraphs
        paragraphs = [paragraph for paragraph in paragraphs if paragraph != ""]
        # Create a list of paragraphs that are not more than 2500 characters
        single_split = []
        split_char_count = 0
        for paragraph in paragraphs:
            if split_char_count + len(paragraph) > 2500:
                audio_split.append(
                    {"paragraphs": single_split, "count": split_char_count}
                )
                single_split = []
                split_char_count = 0
            single_split.append(paragraph)
            split_char_count += len(paragraph)
        audio_split.append({"paragraphs": single_split, "count": split_char_count})

    # Write the split paragraphs to files
    for i, split in enumerate(audio_split):
        paragraphs = split["paragraphs"]
        count = split["count"]
        # Convert i to a string and pad it with 0s
        i = str(i).zfill(3)
        with open(
            os.path.join(output_dir, essay_filename, f"{i} - {count}.txt"), "w"
        ) as split_file:
            split_file.write("\n".join(paragraphs) + "\n")
