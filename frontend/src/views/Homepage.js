import { motion } from 'framer-motion';
import bg from '../assets/bg.png';
import Footer from '../components/Footer';
import Pricing from '../components/Pricing';
import Figure from '../components/Figure';
import WayChoose from '../components/WayChoose';

function HomePage() {
  return (
    <div className="bg-white">
      <div className="w-[1500px] max-h-[850px] relative">
        <div className="flex justify-center items-center text-black">
          <div className="mx-10 w-[645px] h-[493px] flex-1">
            <motion.h1
              className="font-bold text-6xl"
              initial={{ opacity: 0, y: -50 }} // Initial state
              animate={{ opacity: 1, y: 0 }} // Animate to this state
              transition={{ duration: 0.8 }} // Animation duration
            >
              Elevate your workout
            </motion.h1>
            <motion.p
              className="text-base"
              initial={{ opacity: 0, y: 20 }} // Initial state
              animate={{ opacity: 1, y: 0 }} // Animate to this state
              transition={{ duration: 0.8, delay: 0.2 }} // Animation duration with a delay
            >
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
              enim ad minim veniam, quis nostrud exercitation ullamco laboris
              nisi ut aliquip ex ea commodo consequat.
            </motion.p>
          </div>
          <div className="flex-1 flex justify-center relative">
            <motion.img
              className="z-[1]"
              src={bg}
              style={{ width: '671.67px', height: '650px' }}
              alt="Background"
              initial={{ scale: 0 }} // Initial state for image scaling
              animate={{ scale: 1 }} // Animate to normal size
              transition={{ duration: 0.8, delay: 0.4 }} // Animation duration with a delay
            />
            <div className="bg-gray-900 w-[490px] h-[850px] absolute right-[-19px] top-[-200px] z-[0]"></div>
          </div>
        </div>
      </div>
      <Figure />
      <WayChoose />
      {/* <Pricing /> */}
      <Footer />
    </div>
  );
}

export default HomePage;
