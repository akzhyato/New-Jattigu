import { useState, useContext } from 'react';
import { Link, useHistory } from 'react-router-dom';
import AuthContext from '../context/AuthContext';

function Registerpage() {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [password2, setPassword2] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');
  const [weight, setWeight] = useState('');
  const [height, setHeight] = useState('');
  const [fitnessGoal, setFitnessGoal] = useState('');

  const { registerUser } = useContext(AuthContext);
  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await registerUser(
      email,
      username,
      password,
      password2,
      age,
      gender,
      weight,
      height,
      fitnessGoal
    );
  };

  return (
    <div>
      <section className="min-h-screen bg-gray-200 flex items-center justify-center">
        <div className="container mx-auto px-4 py-8">
          <div className="max-w-5xl mx-auto bg-white rounded-lg shadow-lg">
            <div className="grid grid-cols-1 md:grid-cols-2">
              <div className="hidden md:block">
                <img
                  src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img1.webp"
                  alt="login form"
                  className="h-full w-full object-cover rounded-l-lg"
                />
              </div>
              <div className="flex items-center">
                <div className="p-8 w-full">
                  <form onSubmit={handleSubmit}>
                    <div className="text-center mb-6">
                      <h2 className="text-2xl font-bold text-gray-800">
                        Welcome to <b>Desphixs 👋</b>
                      </h2>
                      <p className="text-gray-600">Sign Up</p>
                    </div>
                    <div className="space-y-4">
                      <input
                        type="email"
                        placeholder="Email Address"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        onChange={(e) => setEmail(e.target.value)}
                      />
                      <input
                        type="text"
                        placeholder="Username"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        onChange={(e) => setUsername(e.target.value)}
                      />
                      <input
                        type="password"
                        placeholder="Password"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        onChange={(e) => setPassword(e.target.value)}
                      />
                      <input
                        type="password"
                        placeholder="Confirm Password"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        onChange={(e) => setPassword2(e.target.value)}
                      />
                      <input
                        type="number"
                        placeholder="Age"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        onChange={(e) => setAge(e.target.value)}
                      />
                      <select
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        onChange={(e) => setGender(e.target.value)}
                      >
                        <option
                          value=""
                          disabled
                          selected
                        >
                          Select Gender
                        </option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                      </select>
                      <input
                        type="number"
                        placeholder="Weight (kg)"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        onChange={(e) => setWeight(e.target.value)}
                      />
                      <input
                        type="number"
                        placeholder="Height (cm)"
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        onChange={(e) => setHeight(e.target.value)}
                      />
                      <select
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-indigo-500"
                        onChange={(e) => setFitnessGoal(e.target.value)}
                      >
                        <option
                          value=""
                          disabled
                          selected
                        >
                          Select Fitness Goal
                        </option>
                        <option value="lose_weight">Lose Weight</option>
                        <option value="build_muscle">Build Muscle</option>
                        <option value="stay_fit">Stay Fit</option>
                      </select>
                    </div>
                    <button
                      type="submit"
                      className="w-full bg-indigo-600 text-white p-3 rounded-lg mt-6 hover:bg-indigo-700"
                    >
                      Register
                    </button>
                    <div className="text-center mt-4 text-gray-600">
                      Already have an account?{' '}
                      <Link
                        to="/login"
                        className="text-indigo-500"
                      >
                        Login Now
                      </Link>
                    </div>
                  </form>
                  <div className="text-center mt-4 text-sm text-gray-500">
                    <a
                      href="#!"
                      className="hover:underline"
                    >
                      Terms of use
                    </a>{' '}
                    |{' '}
                    <a
                      href="#!"
                      className="hover:underline"
                    >
                      Privacy policy
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Registerpage;
