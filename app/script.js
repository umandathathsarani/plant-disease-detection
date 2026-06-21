// THEME SWITCHER LOGIC 
const themeSelector = document.getElementById('themeSelector');
themeSelector.addEventListener('change', function() {
    document.documentElement.setAttribute('data-theme', this.value);
});

// APPLICATION INFERENCE LOGIC 
const fileInput = document.getElementById('fileInput');
const preview = document.getElementById('preview');
const uploadText = document.getElementById('uploadText');
const predictBtn = document.getElementById('predictBtn');
const resultPanel = document.getElementById('resultPanel');
const spinner = document.getElementById('spinner');
const diseaseOutput = document.getElementById('diseaseOutput');
const confidenceOutput = document.getElementById('confidenceOutput');

// Handle leaf photo selection and visual card preview
fileInput.addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block';
            uploadText.style.display = 'none';
            predictBtn.disabled = false;
            resultPanel.style.display = 'none';
        }
        reader.readAsDataURL(file);
    }
});

// Transmit image payload data to the FastAPI endpoint
predictBtn.addEventListener('click', async function() {
    const file = fileInput.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    // Toggle visual loading states
    predictBtn.style.display = 'none';
    spinner.style.display = 'block';
    resultPanel.style.display = 'none';

    try {
        const response = await fetch('http://127.0.0.1:8000/predict', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) throw new Error('API server issue encountered');

        const data = await response.json();
        
        // Render target diagnosis details with formatted spacing strings
        diseaseOutput.innerText = data.disease.replace(/___/g, ' - ').replace(/_/g, ' ');
        confidenceOutput.innerText = `Confidence Level: ${data.confidence}%`;
        resultPanel.style.display = 'block';
    } catch (error) {
        alert('Error running inference: ' + error.message);
    } finally {
        // Reset element layout visibility status
        spinner.style.display = 'none';
        predictBtn.style.display = 'block';
    }
});