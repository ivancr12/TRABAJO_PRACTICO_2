
def clean_missing_values(data, strategy='mean'):
    """
    Handle missing values in dataset.
    
    Args:
        data: Input data
        strategy: 'mean', 'median', or 'drop'
    
    Returns:
        Cleaned data
    """
    print(f"Cleaning missing values using {strategy} strategy")
    # Simulated cleaning
    return data

def normalize_data(data, method='minmax'):
    """
    Normalize data to specific range.
    
    Args:
        data: Input data
        method: 'minmax' or 'standard'
    
    Returns:
        Normalized data
    """
    print(f"Normalizing data using {method} method")
    # Simulated normalization
    return data

if __name__ == "__main__":
    print("Preprocessing module ready")

def remove_outliers(data, threshold=3.0):
    """
    Remove outliers using Z-score method.
    
    Args:
        data: Input data
        threshold: Z-score threshold (default 3.0)
    
    Returns:
        Data without outliers
    """
    print(f"Removing outliers with Z-score threshold {threshold}")
    # Simulated outlier removal
    return data

def split_train_test(data, test_size=0.2):
    """
    Split data into training and testing sets.
    
    Args:
        data: Input data
        test_size: Proportion for test set (default 0.2)
    
    Returns:
        train_data, test_data
    """
    print(f"Splitting data: test_size={test_size}")
    # Simulated split
    split_point = int(len(data) * (1 - test_size))
    return data[:split_point], data[split_point:]
