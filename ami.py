import numpy as np
import matplotlib.pyplot as plt

def ami_encode(bits):
    prev_level = -1
    encoded = []
    for bit in bits:
        if bit == 1:
            prev_level *= -1
            encoded.append(prev_level)
        else:
            encoded.append(0)
    return encoded

def pseudo_ternary_encode(bits):
    prev_level = -1
    encoded = []
    for bit in bits:
        if bit == 0:
            prev_level *= -1
            encoded.append(prev_level)
        else:
            encoded.append(0)
    return encoded

def b8zs_encode(bits):
    encoded = []
    prev_level = -1
    zero_count = 0
    
    for bit in bits:
        if bit == 0:
            zero_count += 1
            if zero_count == 8:
                # Replace last 8 zeros with B8ZS pattern
                encoded[-7:] = []  # Remove previous 7 zeros
                # B8ZS pattern: 000+-0-+
                if prev_level == 1:
                    encoded.extend([0, 0, 0, 1, -1, 0, -1, 1])
                else:
                    encoded.extend([0, 0, 0, -1, 1, 0, 1, -1])
                prev_level = encoded[-1]  # Update prev_level after violation
                zero_count = 0
            else:
                encoded.append(0)
        else:
            prev_level *= -1
            encoded.append(prev_level)
            zero_count = 0
            
    return encoded

def hdb3_encode(bits):
    encoded = []
    encoded_labels = []  # For debugging/visualization
    pulse_count = 0  # Count of non-zero pulses (replaces Violaciones)
    prev_pulse = 0  # Previous non-zero pulse (replaces pulsoAnterior)
    violation_pulse = 0  # Last violation pulse (replaces pulsoViolacion)
    zero_count = 0  # Counter for zeros (replaces contador)
    
    for bit in bits:
        if bit == 1:
            if prev_pulse == 1:
                encoded.append(-1)
                encoded_labels.append(-1)
                prev_pulse = -1
                violation_pulse = -1
                pulse_count += 1
            elif prev_pulse == -1:
                encoded.append(1)
                encoded_labels.append(1)
                prev_pulse = 1
            elif prev_pulse == 0:
                encoded.append(1)
                encoded_labels.append(1)
                prev_pulse = 1
            zero_count = 0
            
        else:  # bit == 0
            zero_count += 1
            if zero_count == 4:
                # Remove last three zeros
                encoded = encoded[:-3]
                encoded_labels = encoded_labels[:-3]
                
                if pulse_count % 2 == 0:
                    # B00V pattern
                    violation_pulse = prev_pulse * -1
                    encoded.extend([violation_pulse, 0, 0, violation_pulse])
                    encoded_labels.extend(["B", 0, 0, "V"])
                    pulse_count += 1
                    prev_pulse = violation_pulse
                else:
                    # 000V pattern
                    encoded.extend([0, 0, 0, violation_pulse])
                    encoded_labels.extend([0, 0, 0, "V"])
                    pulse_count += 1
                
                zero_count = 0
            else:
                encoded.append(0)
                encoded_labels.append(0)
    
    return encoded

def plot_signals(binary_seq, encoded_signals, titles):
    num_plots = len(encoded_signals) + 1
    plt.figure(figsize=(12, 8))
    
    # Plot original binary sequence
    plt.subplot(num_plots, 1, 1)
    plt.title('Original Data')
    plt.ylim(-0.5, 1.5)
    plt.yticks([0, 1], ['0', '1'])
    plt.xticks(range(len(binary_seq)), binary_seq, fontsize=10)
    plt.xlabel('Bit Position')
    plt.ylabel('Bit Value')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.step(range(len(binary_seq)), binary_seq, where='post', linewidth=2, color='black')
    
    for i, bit in enumerate(binary_seq):
        plt.text(i+0.5, -0.3, str(bit), horizontalalignment='center', fontsize=10)
    
    # Plot encoded signals
    colors = ['blue', 'orange', 'red', 'green']
    for i, (encoded_signal, title) in enumerate(zip(encoded_signals, titles)):
        plt.subplot(num_plots, 1, i + 2)
        plt.title(title)
        plt.ylim(-1.5, 1.5)
        plt.yticks([-1, 0, 1], ['Low', '0', 'High'])
        plt.xticks(range(len(binary_seq)), binary_seq, fontsize=10)
        plt.xlabel('Bit Position')
        plt.ylabel('Signal Level')
        plt.grid(True, linestyle='--', alpha=0.6)
        
        plt.step(range(len(encoded_signal)), encoded_signal, where='post',
                linewidth=2, color=colors[i % len(colors)])
        plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        
        for j, bit in enumerate(binary_seq):
            plt.text(j+0.5, -1.3, str(bit), horizontalalignment='center', fontsize=10)
    
    plt.tight_layout()
    plt.show()
    
    
def main():
    # Test the code with a sample binary sequence
    binary_input = input("Enter a binary sequence (e.g., 1010000000): ")
    
    # Convert input string to list of integers
    binary_sequence = [int(bit) for bit in binary_input if bit in '01']
    
    # Generate encoded signals
    ami_encoded = ami_encode(binary_sequence)
    pseudo_ternary_encoded = pseudo_ternary_encode(binary_sequence)
    b8zs_encoded = b8zs_encode(binary_sequence)
    hdb3_encoded = hdb3_encode(binary_sequence)
    
    # Plot all signals
    plot_signals(binary_sequence,
                [ami_encoded, pseudo_ternary_encoded, b8zs_encoded, hdb3_encoded],
                ["AMI Line Coding", "Pseudo-Ternary", "B8ZS", "HDB3"])

# Call the main function
if __name__ == "__main__":
    main()