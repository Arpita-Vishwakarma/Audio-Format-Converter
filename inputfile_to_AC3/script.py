from pydub import AudioSegment
import os

def convert_aac_to_ac3(input_file):
    # Generate output file path
    output_file = os.path.splitext(input_file)[0] + "_converted.ac3"

    # Load AAC file using pydub
    audio = AudioSegment.from_file(input_file, format="aac")

    # Convert audio to AC3
    audio.export(output_file, format="ac3")

    print(f"Conversion complete. Output file: {output_file}")

if __name__ == "__main__":
    # Provide the path to your AAC file
    input_aac_file = r"C:\Users\DELL\PYTHON PROJECTS\audio_con\AAC_to_AC3\sample1.aac"

    # Check if the file exists before conversion
    if os.path.exists(input_aac_file):
        # Convert AAC to AC3
        convert_aac_to_ac3(input_aac_file)
    else:
        print("ERROR")
        print(f"Error: File not found - {input_aac_file}")
