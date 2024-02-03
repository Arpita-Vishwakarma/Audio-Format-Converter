from pydub import AudioSegment
import os

def convert_aac_to_aif(input_file):
    # Generate output file path
    output_file = os.path.splitext(input_file)[0] + "_converted.aif"

    # Load AAC file using pydub
    audio = AudioSegment.from_file(input_file, format="aac")

    # Convert audio to AIF
    audio.export(output_file, format="aif")

    print(f"Conversion complete. Output file: {output_file}")

if __name__ == "__main__":
    # Provide the path to your AAC file
    input_aac_file = r"C:\Users\DELL\PYTHON PROJECTS\audio_con\AAC\AAC_to_AIF\sample1.aac"

    # Check if the file exists before conversion
    if os.path.exists(input_aac_file):
        # Convert AAC to AIF
        convert_aac_to_aif(input_aac_file)
    else:
        print("Error: File not found -", input_aac_file)
