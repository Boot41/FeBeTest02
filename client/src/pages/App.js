import React, { useEffect, useState } from 'react'; // Import React and necessary hooks
import Header from '../components/Header'; // Import Header component
import Footer from '../components/Footer'; // Import Footer component
import Sidebar from '../components/Sidebar'; // Import Sidebar component

const App = () => {
    const [data, setData] = useState([]); // State to store API data
    const [loading, setLoading] = useState(true); // Loading state
    const [error, setError] = useState(null); // Error state

    useEffect(() => {
        const fetchData = async () => { // Function to fetch data from API
            try {
                const response = await fetch('http://localhost:8080'); // Fetch data
                if (!response.ok) throw new Error('Network response was not ok'); // Error handling
                const result = await response.json(); // Parse JSON response
                setData(result); // Update state with fetched data
            } catch (error) {
                setError(error); // Set error state
            } finally {
                setLoading(false); // Set loading to false once done
            }
        };

        fetchData(); // Call the fetch function
    }, []); // Empty dependency array to run once on mount

    return (
        <div className="flex flex-col min-h-screen"> {/* Main container with flex layout */}
            <Header /> {/* Render Header component */}
            <div className="flex flex-1"> {/* Flex container for Sidebar and Main content */}
                <Sidebar /> {/* Render Sidebar component */}
                <main className="flex-1 p-4"> {/* Main content area with padding */}
                    {loading && <p>Loading...</p>} {/* Display loading text */}
                    {error && <p>Error: {error.message}</p>} {/* Display error message */}
                    {!loading && !error && (
                        <div>
                            {/* Render your main content using the fetched data */}
                            {data.map(item => (
                                <div key={item.id} className="mb-4 p-4 border rounded"> {/* Item card */}
                                    <h2 className="font-bold">{item.title}</h2> {/* Title */}
                                    <p>{item.description}</p> {/* Description */}
                                </div>
                            ))}
                        </div>
                    )}
                </main>
            </div>
            <Footer /> {/* Render Footer component */}
        </div>
    );
};

export default App; // Export App component for use in the application