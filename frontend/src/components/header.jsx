import React from "react";
export default function Header({ firstName, lastName }) {
    return (
        <nav className="navbar bg-body-tertiary">
            <div className="container-fluid">
                <span className="navbar-brand mb-0 h1">Investment App</span>
                <span className="navbar-text">{firstName} {lastName}</span>
            </div>
        </nav>
    );
}