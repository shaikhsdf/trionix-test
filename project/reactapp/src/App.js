import logo from './logo.svg';
import './App.css';
import {Home} from './Home';
import {Student} from './Student';
import {BrowserRouter, Route, Switch,NavLink} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    <div className="App container">
      <div className="container">
          <h3>Student CRUD Syten</h3>
      </div>
        
      <nav className="navbar navbar-expand-sm bg-light navbar-dark">
        <ul className="navbar-nav">
          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary" to="/home">
              Home
            </NavLink>
          </li>
          {/* <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary" to="/student">
              Add Student
            </NavLink>
          </li> */}
          <li className="nav-item- m-1">
            <NavLink className="btn btn-light btn-outline-primary" to="/student">
              Student List
            </NavLink>
          </li>
        </ul>
      </nav>

      <Switch>
        <Route path='/home' component={Home}/>
        {/* <Route path='/student' component={Student}/> */}
        <Route path='/student' component={Student}/>
      </Switch>
      <small>Developed and Designed by <a href="https://shaikhsdf.github.io/">Sadaf Shaikh</a></small>
    </div>
    </BrowserRouter>
  );
}

export default App;
