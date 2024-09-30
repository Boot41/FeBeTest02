import React, { useState } from 'react';
import { FaHome, FaUser, FaCog } from 'react-icons/fa';

const Sidebar = () => {
    const [isOpen, setIsOpen] = useState(true); // State to handle sidebar visibility

    const toggleSidebar = () => {
        setIsOpen(!isOpen); // Toggle sidebar function
    };

    return (
        <div className={`fixed top-0 left-0 h-full transition-all duration-300 ${isOpen ? 'w-64' : 'w-16'} bg-gray-800 text-white`}>
            <button onClick={toggleSidebar} className="p-4 focus:outline-none">
                {isOpen ? '▸' : '▴'} {/* Toggle icon for user to expand/collapse sidebar */}
            </button>
            <nav className={`flex flex-col items-start mt-5 ${isOpen ? 'block' : 'hidden'}`}>
                <a href="#home" className="flex items-center py-2 px-4 hover:bg-gray-700 w-full">
                    <FaHome className="mr-3" /> {isOpen && <span>Home</span>}
                </a>
                <a href="#profile" className="flex items-center py-2 px-4 hover:bg-gray-700 w-full">
                    <FaUser className="mr-3" /> {isOpen && <span>Profile</span>}
                </a>
                <a href="#settings" className="flex items-center py-2 px-4 hover:bg-gray-700 w-full">
                    <FaCog className="mr-3" /> {isOpen && <span>Settings</span>}
                </a>
            </nav>
        </div>
    );
};

export default Sidebar;