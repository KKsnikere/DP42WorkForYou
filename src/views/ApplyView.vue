  <template>
      <div class="max-w-lg mx-auto p-6 bg-white rounded-lg shadow-md">
        <h2 class="text-2xl font-bold mb-6 text-center">Apply Form</h2>
        
        <!-- Form -->
        <form @submit.prevent="handleSubmit">
          <!-- Name Field -->
          <div class="mb-4">
            <label for="name" class="block text-gray-700 font-medium mb-2">First Name</label>
            <input 
              type="text" 
              id="name" 
              v-model="form.name" 
              placeholder="Enter your first name"
              class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-accent"
              required
            />
          </div>
          
          <!-- Surname Field -->
          <div class="mb-4">
            <label for="surname" class="block text-gray-700 font-medium mb-2">Surname</label>
            <input 
              type="text" 
              id="surname" 
              v-model="form.surname" 
              placeholder="Enter your surname"
              class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-accent"
              required
            />
          </div>
          
          <!-- Phone Number Field -->
          <div class="mb-4">
            <label for="phone" class="block text-gray-700 font-medium mb-2">Phone Number</label>
            <input 
              type="tel" 
              id="phone" 
              v-model="form.phone" 
              placeholder="Enter your phone number"
              class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-accent"
              required
            />
          </div>
          
          <!-- Email Field -->
          <div class="mb-4">
            <label for="email" class="block text-gray-700 font-medium mb-2">Email</label>
            <input 
              type="email" 
              id="email" 
              v-model="form.email" 
              placeholder="Enter your email address"
              class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-accent"
              required
            />
          </div>
          
          <!-- Message Field -->
          <div class="mb-4">
            <label for="message" class="block text-gray-700 font-medium mb-2">Message</label>
            <textarea 
              id="message" 
              v-model="form.message" 
              placeholder="Enter your message" 
              class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-accent"
              rows="5"
              required
            ></textarea>
          </div>
          
          <!-- Upload Button (Smaller) -->
          <div class="mb-4">
                <label for="files" class="block text-gray-700 font-medium mb-2">Upload Files</label>
                <input
                    type="file"
                    id="files"
                    @change="handleFileUpload"
                    class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-accent"
                    multiple
                />
          </div>
    
          <!-- Apply Button -->
          <div class="mb-6">
            <button 
              type="button" 
              class="w-full p-3 text-white bg-accent rounded-lg focus:outline-none hover:bg-primary"
              @click="handleSubmit"
            >
              Apply
            </button>
          </div>
          
          <!-- Submit Button -->
          <div>
            <button 
              type="submit" 
              class="w-full p-3 text-white bg-green-600 rounded-lg focus:outline-none hover:bg-green-500"
            >
              Submit Application
            </button>
          </div>
        </form>
      </div>
    </template>
    
    <script>
    export default {
        data() {
            return {
                form: {
                    name: '',
                    surname: '',
                    phone: '',
                    email: '',
                    message: '',
                    files: [] // Array to hold uploaded files
                }
            };
        },
        methods: {
            handleFileUpload(event) {
                // Convert the FileList to an Array and store in form.files
                this.form.files = Array.from(event.target.files);
            },
            async handleSubmit() {
                const formData = new FormData();
                // Append all form fields to FormData
                Object.keys(this.form).forEach(key => {
                    if (Array.isArray(this.form[key])) {
                        this.form[key].forEach(file => {
                            formData.append('files', file); // Append each file
                        });
                    } else {
                        formData.append(key, this.form[key]);
                    }
                });
    
                try {
                    const response = await fetch('http://localhost:5000/apply', {
                        method: 'POST',
                        body: formData,
                    });
    
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
    
                    const result = await response.json();
                    console.log("Response from server:", result);
                    alert(result.message);
    
                    // Reset form after submission
                    this.form = {
                        name: '',
                        surname: '',
                        phone: '',
                        email: '',
                        message: '',
                        files: []
                    };
    
                } catch (error) {
                    console.error('Error submitting form:', error);
                    alert('Failed to submit application.');
                }
            }
        }
    };
    </script>