import subprocess

def list_audio_sinks():
    """List available audio output devices (sinks)."""
    result = subprocess.run(['pactl', 'list', 'short', 'sinks'], capture_output=True, text=True)
    print("Available audio output devices:")
    print(result.stdout)

def set_default_sink(sink_name):
    """Set the default audio output device."""
    subprocess.run(['pactl', 'set-default-sink', sink_name])

def get_active_sink_name():
    """Get the name of the current default audio output device."""
    result = subprocess.run(['pactl', 'info'], capture_output=True, text=True)
    lines = result.stdout.split('\n')
    for line in lines:
        if "Default Sink" in line:
            return line.split(': ')[1]
    return "Unknown"

def main():
    list_audio_sinks()
    current_sink = get_active_sink_name()
    print(f"Current default audio output device: {current_sink}")
    sink_name = input("Enter the name of the audio device to set as default: ")
    set_default_sink(sink_name)
    print(f"Default audio device set to {sink_name}")

if __name__ == "__main__":
    main()
