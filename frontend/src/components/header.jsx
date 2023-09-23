export default function Header({ first_name, last_name }) {
    return (
        <nav className="navbar bg-body-tertiary">
            <div className="container-fluid">
                <span className="navbar-brand mb-0 h1">Investment App</span>
                <span className="navbar-text">{first_name} {last_name}</span>
            </div>
        </nav>
    );
}