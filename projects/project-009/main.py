def OutputSummary(N,Sum,Mean,Minimum,Maximum,Range):
    # Calculate statistics
    print(f"""
          ===================
          DATA SUMMARY REPORT
          ===================
          
          Number of observation: {N}
          Sum: {Sum}
          Mean: {Mean}
          Minimum: {Minimum}
          Maximum: {Maximum}
          Range: {Range}
          """)

def main():
    # Prompt the user for input
    input_data = [10, 20, 30, 40, 50]
    N = len(input_data)
    Sum = sum(input_data)
    Mean = Sum/N
    Minimum = min(input_data)
    Maximum = max(input_data)
    Range = Maximum - Minimum
    
    # Output the summary
    OutputSummary(N,Sum,Mean,Minimum,Maximum,Range)


if __name__ == "__main__":
    main()
