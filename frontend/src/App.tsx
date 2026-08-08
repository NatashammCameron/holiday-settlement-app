import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import HolidayDetails from "./pages/HolidayDetails";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route
                    path="/"
                    element={<Dashboard />}
                />

                <Route
                    path="/holiday/:id"
                    element={<HolidayDetails />}
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;