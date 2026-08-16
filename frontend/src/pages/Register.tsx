import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

import { register } from "../services/authService";

export default function Register() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const navigate = useNavigate();

    const handleRegister = async () => {
        try {
            await register(
                email,
                password
            );

            navigate("/login");
        }
        catch {
            alert(
                "Registration failed"
            );
        }
    };

    return (
        <div>
            <h1>Register</h1>

            <input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) =>
                    setEmail(
                        e.target.value
                    )
                }
            />

            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) =>
                    setPassword(
                        e.target.value
                    )
                }
            />

            <button
                onClick={handleRegister}
            >
                Register
            </button>

            <p>
                Already have an account?{" "}
                <Link to="/login">
                    Login
                </Link>
            </p>
        </div>
    );
}