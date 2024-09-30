import React from 'react';

const Footer = () => {
    return (
        <footer className="bg-gray-800 text-white p-4">
            <div className="container mx-auto flex justify-between">
                <div>
                    <a href="/privacy-policy" className="hover:underline">Privacy Policy</a>
                </div>
                <div>
                    <a href="/terms-of-service" className="hover:underline">Terms of Service</a>
                </div>
                <div>
                    <a href="/contact" className="hover:underline">Contact Us</a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;