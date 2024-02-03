from pydub import AudioSegment
import os
import aifc

def convert_aac_to_aifc(input_file):
    # Generate output file path
    output_file = os.path.splitext(input_file)[0] + "_converted.aifc"

    # Load AAC file using pydub
    audio = AudioSegment.from_file(input_file, format="aac")

    # Convert audio to AIFC using aifc module
    with aifc.open(output_file, 'wb') as aifc_file:
        aifc_file.setframerate(audio.frame_rate)
        aifc_file.setnchannels(audio.channels)
        aifc_file.setsampwidth(audio.sample_width)
        aifc_file.writeframes(audio.raw_data)

    print(f"Conversion complete. Output file: {output_file}")

if __name__ == "__main__":
    # Provide the path to your AAC file
    input_aac_file = r"C:\Users\DELL\PYTHON PROJECTS\audio_con\AAC\AAC_to_AIFC\sample1.aac"

    # Check if the file exists before conversion
    if os.path.exists(input_aac_file):
        # Convert AAC to AIFC
        convert_aac_to_aifc(input_aac_file)
    else:
        print("Error: File not found -", input_aac_file)
