import numpy as np
import joblib

# Load scaler
scaler = joblib.load("scaler_pca.joblib")

def preprocess_input(input_dict):
    """
    Preprocess input data for the student success prediction model.
    
    Args:
        input_dict: Dictionary containing all required features
    
    Returns:
        Scaled numpy array ready for model prediction
    """
    
    # Feature validation - check if all required features are present
    required_features = [
        'Marital_status', 'Application_mode', 'Application_order', 'Course',
        'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
        'Nacionality', 'Mothers_qualification', 'Fathers_qualification',
        'Mothers_occupation', 'Fathers_occupation', 'Admission_grade',
        'Displaced', 'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date',
        'Gender', 'Scholarship_holder', 'Age_at_enrollment', 'International',
        'Curricular_units_1st_sem_credited'
    ]
    
    # Check for missing features
    missing_features = [f for f in required_features if f not in input_dict]
    if missing_features:
        raise ValueError(f"Missing required features: {missing_features}")
    
    # Validate feature values against allowed ranges
    feature_ranges = {
        'Marital_status': [1, 2, 3, 4, 5, 6],
        'Application_mode': [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57],
        'Application_order': [0, 1, 2, 3, 4, 5, 6, 9],
        'Course': [33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991],
        'Daytime_evening_attendance': [0, 1],
        'Previous_qualification': [1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 19, 38, 39, 40, 42, 43],
        'Nacionality': [1, 2, 6, 11, 13, 14, 17, 21, 22, 24, 25, 26, 32, 41, 62, 100, 101, 103, 105, 108, 109],
        'Mothers_qualification': [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 18, 19, 22, 26, 27, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
        'Fathers_qualification': [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 18, 19, 20, 22, 25, 26, 27, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
        'Mothers_occupation': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 122, 123, 125, 131, 132, 134, 141, 143, 144, 151, 152, 153, 171, 173, 175, 191, 192, 193, 194],
        'Fathers_occupation': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 101, 102, 103, 112, 114, 121, 122, 123, 124, 131, 132, 134, 135, 141, 143, 144, 151, 152, 153, 154, 161, 163, 171, 172, 174, 175, 181, 182, 183, 192, 193, 194, 195],
        'Displaced': [0, 1],
        'Educational_special_needs': [0, 1],
        'Debtor': [0, 1],
        'Tuition_fees_up_to_date': [0, 1],
        'Gender': [0, 1],
        'Scholarship_holder': [0, 1],
        'International': [0, 1],
        'Curricular_units_1st_sem_credited': list(range(0, 21))  # 0 to 20
    }
    
    # Validate categorical features
    for feature, valid_values in feature_ranges.items():
        if feature in input_dict and input_dict[feature] not in valid_values:
            raise ValueError(f"Invalid value for {feature}: {input_dict[feature]}. Valid values: {valid_values}")
    
    # Validate continuous features (grades and age)
    if not (95.0 <= input_dict['Previous_qualification_grade'] <= 190.0):
        raise ValueError(f"Previous_qualification_grade must be between 95.0 and 190.0")
    
    if not (95.0 <= input_dict['Admission_grade'] <= 190.0):
        raise ValueError(f"Admission_grade must be between 95.0 and 190.0")
    
    if not (17 <= input_dict['Age_at_enrollment'] <= 70):
        raise ValueError(f"Age_at_enrollment must be between 17 and 70")
    
    # Create input array in the correct order (adjust based on your model's expected feature order)
    input_array = np.array([
        input_dict['Marital_status'],
        input_dict['Application_mode'],
        input_dict['Application_order'],
        input_dict['Course'],
        input_dict['Daytime_evening_attendance'],
        input_dict['Previous_qualification'],
        input_dict['Previous_qualification_grade'],
        input_dict['Nacionality'],
        input_dict['Mothers_qualification'],
        input_dict['Fathers_qualification'],
        input_dict['Mothers_occupation'],
        input_dict['Fathers_occupation'],
        input_dict['Admission_grade'],
        input_dict['Displaced'],
        input_dict['Educational_special_needs'],
        input_dict['Debtor'],
        input_dict['Tuition_fees_up_to_date'],
        input_dict['Gender'],
        input_dict['Scholarship_holder'],
        input_dict['Age_at_enrollment'],
        input_dict['International'],
        input_dict['Curricular_units_1st_sem_credited']
    ]).reshape(1, -1)
    
    # Apply scaling
    return scaler.transform(input_array)


def create_sample_input():
    """
    Create a sample input dictionary with valid values for testing.
    """
    return {
        'Marital_status': 1,  # Single
        'Application_mode': 17,  # Most common application mode
        'Application_order': 1,  # First choice
        'Course': 9254,  # One of the available courses
        'Daytime_evening_attendance': 1,  # Daytime
        'Previous_qualification': 1,  # Secondary education
        'Previous_qualification_grade': 120.0,  # Good grade
        'Nacionality': 1,  # Portuguese
        'Mothers_qualification': 19,  # Higher education
        'Fathers_qualification': 12,  # Secondary education
        'Mothers_occupation': 5,  # Intermediate level technicians
        'Fathers_occupation': 9,  # Skilled workers
        'Admission_grade': 125.0,  # Good admission grade
        'Displaced': 0,  # Not displaced
        'Educational_special_needs': 0,  # No special needs
        'Debtor': 0,  # Not a debtor
        'Tuition_fees_up_to_date': 1,  # Fees up to date
        'Gender': 1,  # Male
        'Scholarship_holder': 0,  # No scholarship
        'Age_at_enrollment': 20,  # Typical enrollment age
        'International': 0,  # Not international
        'Curricular_units_1st_sem_credited': 6,  # 6 credited units
        'GDP': 1.74,  # Example GDP value
        'Unemployment_rate': 10.8  # Example unemployment rate
    }



# Example usage:
if __name__ == "__main__":
    # Test with sample data
    sample_data = create_sample_input()
    
    try:
        processed_data = preprocess_input(sample_data)
        print("Preprocessing successful!")
        print(f"Input shape: {processed_data.shape}")
        print(f"Sample processed values: {processed_data[0][:5]}...")  # Show first 5 values
    except Exception as e:
        print(f"Error during preprocessing: {e}")
