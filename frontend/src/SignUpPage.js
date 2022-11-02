import React from 'react';
import {useNavigate} from 'react-router-dom'
import './SignUpPage.css';
import './Login_SignUp_box.css'

const SignUpPage = () => {

  return (
    <div className= "contentFrame">
        <div className="container">
          <div className="login_section">
            <form className="form" id="createAccount">
              <h1 className="form__title">Sign Up</h1>
                <div className="form__message form__message--error">Incorrect username/password combination.</div>
                <div className="form__input-group">
                  <input type="text" className="form__input" autofocus placeholder="Username"></input>
                  <div className="form__message form__input-error-message">This is an error message</div>
                </div>
                <div className="form__input-group">
                  <input type="text" className="form__input" autofocus placeholder="Email Address"></input>
                  <div className="form__message form__input-error-message">This is an error message</div>
                </div>
                <div className="form__input-group">
                  <input type="password" className="form__input" autofocus placeholder="Password"></input>
                  <div className="form__input-error-message"></div>
                  <input type="password" className="form__input" autofocus placeholder="Confirm Password"></input>
                </div>
              <button className="form__button" type="submit">Create Account</button>
              <p className="form__text">
                <a className="form__link" href=" ./login">Already have an account?</a>
              </p>
            </form>
          </div>
        </div>
    </div>
    
    
  );
}

export default SignUpPage;
