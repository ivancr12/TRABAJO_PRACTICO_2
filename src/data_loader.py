import pandas as pd
import os

def load_csv(filepath):
    """
    Load a CSV file into a DataFrame.
    
    Args:
        filepath (str): Path to CSV file
        
    Returns:
        pandas.DataFrame: Loaded data
    """
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} not found")
        return None
    
    try:
        data = pd.read_csv(filepath)
        print(f"Successfully loaded {len(data)} rows")
        return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def validate_data(data, required_cols=None):
    """
    Validate dataset structure.
    
    Args:
        data (DataFrame): Data to validate
        required_cols (list): Required column names
        
    Returns:
        bool: True if valid
    """
    if data is None or data.empty:
        return False
    
    if required_cols:
        for col in required_cols:
            if col not in data.columns:
                print(f"Missing required column: {col}")
                return False
    
    return True

# Test example
if __name__ == "__main__":
    # Create sample data for testing
    test_data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [10, 20, 30, 40, 50],
        'target': [0, 1, 0, 1, 0]
    })
    
    # Save sample file
    os.makedirs('data', exist_ok=True)
    test_data.to_csv('data/sample.csv', index=False)
    
    # Test loading
    df = load_csv('data/sample.csv')
    
    # Test validation
    if validate_data(df, ['feature1', 'feature2', 'target']):
        print("Data validation passed")
        print(f"Data shape: {df.shape}")
    else:
        print("Data validation failed")