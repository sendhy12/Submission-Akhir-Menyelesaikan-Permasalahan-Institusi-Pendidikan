import joblib
import numpy as np
from data_preprocessing import preprocess_input

# Load model and encoders
try:
    model = joblib.load('model\gboost_model.joblib')
    print("✅ Model loaded successfully")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

try:
    label_encoder = joblib.load('model/label_encoder.joblib')
    print("✅ Label encoder loaded successfully")
except Exception as e:
    print(f"❌ Error loading label encoder: {e}")
    label_encoder = None

def predict_dropout(processed_input):
    """
    Predict dropout risk for a student.
    
    Args:
        processed_input: Preprocessed input array from preprocess_input()
    
    Returns:
        int: Prediction result (0 = No Dropout, 1 = Dropout)
        or dict: Detailed prediction with probabilities if available
    """
    
    if model is None:
        raise ValueError("Model not loaded properly")
    
    try:
        # Make prediction
        prediction = model.predict(processed_input)
        prediction_result = int(prediction[0])
        
        # Get prediction probabilities if available
        if hasattr(model, 'predict_proba'):
            try:
                probabilities = model.predict_proba(processed_input)
                prob_no_dropout = float(probabilities[0][0])
                prob_dropout = float(probabilities[0][1])
                
                return {
                    'prediction': prediction_result,
                    'probability_no_dropout': prob_no_dropout,
                    'probability_dropout': prob_dropout,
                    'confidence': max(prob_no_dropout, prob_dropout)
                }
            except Exception as e:
                print(f"Warning: Could not get probabilities: {e}")
                return prediction_result
        else:
            return prediction_result
            
    except Exception as e:
        raise Exception(f"Error during prediction: {e}")

def predict_dropout_simple(processed_input):
    """
    Simple version that returns only the prediction (0 or 1).
    Use this if you want to keep your current Streamlit app unchanged.
    """
    if model is None:
        raise ValueError("Model not loaded properly")
    
    try:
        prediction = model.predict(processed_input)
        return int(prediction[0])
    except Exception as e:
        raise Exception(f"Error during prediction: {e}")

def predict_with_interpretation(input_dict):
    """
    Complete prediction function that handles preprocessing and provides interpretation.
    
    Args:
        input_dict: Dictionary with raw input features
    
    Returns:
        dict: Complete prediction results with interpretation
    """
    try:
        # Preprocess input
        processed_input = preprocess_input(input_dict)
        
        # Make prediction
        prediction = model.predict(processed_input)
        prediction_result = int(prediction[0])
        
        # Get probabilities if available
        result = {
            'prediction': prediction_result,
            'prediction_label': 'Dropout' if prediction_result == 1 else 'No Dropout',
            'risk_level': 'High' if prediction_result == 1 else 'Low'
        }
        
        if hasattr(model, 'predict_proba'):
            try:
                probabilities = model.predict_proba(processed_input)
                prob_no_dropout = float(probabilities[0][0])
                prob_dropout = float(probabilities[0][1])
                
                result.update({
                    'probability_no_dropout': prob_no_dropout,
                    'probability_dropout': prob_dropout,
                    'confidence': max(prob_no_dropout, prob_dropout),
                    'confidence_level': 'High' if max(prob_no_dropout, prob_dropout) > 0.8 else 
                                     'Medium' if max(prob_no_dropout, prob_dropout) > 0.6 else 'Low'
                })
            except Exception as e:
                print(f"Warning: Could not get probabilities: {e}")
        
        return result
        
    except Exception as e:
        raise Exception(f"Error in complete prediction: {e}")

# Test function
def test_prediction():
    """
    Test the prediction function with sample data.
    """
    try:
        # Create sample input
        from data_preprocessing import create_sample_input
        sample_data = create_sample_input()
        
        print("🧪 Testing prediction function...")
        print(f"Sample input keys: {list(sample_data.keys())}")
        
        # Test simple prediction
        processed_input = preprocess_input(sample_data)
        simple_result = predict_dropout_simple(processed_input)
        print(f"✅ Simple prediction result: {simple_result}")
        
        # Test detailed prediction
        detailed_result = predict_with_interpretation(sample_data)
        print(f"✅ Detailed prediction result: {detailed_result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    # Run test when script is executed directly
    test_prediction()