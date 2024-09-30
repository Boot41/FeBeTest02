import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { BiSearch, BiChevronDown, BiUser } from 'react-icons/bi';

const Header = () => {
    const [dropdownOpen, setDropdownOpen] = useState(false);
    const [theme, setTheme] = useState('dark');

    const toggleDropdown = () => setDropdownOpen(!dropdownOpen);

    const handleThemeChange = (newTheme) => {
        setTheme(newTheme);
        document.documentElement.setAttribute('data-theme', newTheme);
    };

    return (
        <header className={`bg-gray-800 text-white flex justify-between items-center p-4`}>
            <div className="flex items-center">
                <img src="/logo.png" alt="Company Logo" className="h-8 mr-3" />
                <span className="text-xl">Company Name</span>
            </div>
            <div className="flex items-center">
                <input 
                    type="text" 
                    placeholder="Search..." 
                    className="bg-gray-700 text-white rounded-lg px-3 py-1 shadow-md focus:outline-none" 
                />
                <BiSearch className="ml-2 cursor-pointer" />
                <div className="relative">
                    <BiUser className="ml-4 cursor-pointer" onClick={toggleDropdown} />
                    {dropdownOpen && (
                        <div className="absolute right-0 bg-white text-black shadow-lg mt-2 rounded-lg z-10">
                            <ul>
                                <li onClick={() => console.log('Profile Settings')} className="px-4 py-2 hover:bg-gray-200">Profile Settings</li>
                                <li onClick={() => console.log('Logout')} className="px-4 py-2 hover:bg-gray-200">Logout</li>
                                <li onClick={() => handleThemeChange(theme === 'dark' ? 'light' : 'dark')} className="px-4 py-2 hover:bg-gray-200">
                                    Theme: {theme === 'dark' ? 'Light' : 'Dark'}
                                </li>
                            </ul>
                        </div>
                    )}
                </div>
            </div>
        </header>
    );
};

export default Header;

import React from 'react';

const Footer = () => {
    return (
        <footer className="bg-gray-800 text-white p-4">
            <div className="flex justify-between">
                <Link to="/privacy" className="hover:underline">Privacy Policy</Link>
                <Link to="/terms" className="hover:underline">Terms of Service</Link>
            </div>
        </footer>
    );
};

export default Footer;

import React from 'react';
import { AiOutlineHome, AiOutlineSetting } from 'react-icons/ai';

const Sidebar = () => {
    return (
        <aside className="bg-gray-800 text-white fixed h-full w-64">
            <nav className="flex flex-col p-4">
                <a href="/home" className="flex items-center py-2 hover:bg-gray-700 rounded">
                    <AiOutlineHome className="mr-2" /> Home
                </a>
                <a href="/settings" className="flex items-center py-2 hover:bg-gray-700 rounded">
                    <AiOutlineSetting className="mr-2" /> Settings
                </a>
                {/* Add more nav items as needed */}
            </nav>
        </aside>
    );
};

export default Sidebar;

import React from 'react';
import Header from './Header'; // Import imported Header component
import Footer from './Footer'; // Import imported Footer component
import Sidebar from './Sidebar'; // Import imported Sidebar component

const App = () => {
    return (
        <div className="flex flex-col min-h-screen">
            <Header />
            <div className="flex flex-1">
                <Sidebar />
                <main className="flex-1 p-4">
                    {/* Main content goes here */}
                </main>
            </div>
            <Footer />
        </div>
    );
};

export default App;