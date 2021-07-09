-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 27, 2021 at 05:10 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mobile_sales`
--

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
CREATE TABLE IF NOT EXISTS `brand` (
  `brandid` int(8) NOT NULL,
  `brandname` varchar(50) NOT NULL,
  PRIMARY KEY (`brandid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `brand`
--

INSERT INTO `brand` (`brandid`, `brandname`) VALUES
(1, 'Apple'),
(2, 'Samsung'),
(3, 'OnePlus'),
(4, 'Google'),
(5, 'Nokia'),
(6, 'Asus'),
(7, 'Sony');

-- --------------------------------------------------------

--
-- Table structure for table `logindetails`
--

DROP TABLE IF EXISTS `logindetails`;
CREATE TABLE IF NOT EXISTS `logindetails` (
  `userid` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL DEFAULT 'User',
  `adminkey` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `logindetails`
--

INSERT INTO `logindetails` (`userid`, `password`, `type`, `adminkey`) VALUES
('admin', 'admin123', 'Admin', 'anirudh'),
('ani', '123', 'User', NULL),
('ariba', '123', 'User', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `modeldetails`
--

DROP TABLE IF EXISTS `modeldetails`;
CREATE TABLE IF NOT EXISTS `modeldetails` (
  `modelnumber` int(8) NOT NULL,
  `brandid` int(8) NOT NULL,
  `modelname` varchar(50) NOT NULL,
  `price` float NOT NULL,
  `features` varchar(100) NOT NULL,
  `quantity` int(3) NOT NULL,
  PRIMARY KEY (`modelnumber`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `modeldetails`
--

INSERT INTO `modeldetails` (`modelnumber`, `brandid`, `modelname`, `price`, `features`, `quantity`) VALUES
(1, 1, 'iPhone X', 34000, 'OLED display, Glass body, Facial Recognition, Wireless charging.', 48),
(2, 1, 'iPhone XR', 39000, 'Liquid Retina HD display, Splash Resistant IP67, A12 bionic chip.', 46),
(3, 1, 'iPhone 11', 68000, 'A13 bionic chip, 4GB RAM, 12MP + 12MP dual Camera.', 50),
(4, 1, 'iPhone 11 Pro Max', 106000, 'Super Retina XDR display, A13 bionic chip, Triple Camera setup.', 49),
(5, 2, 'S10', 59000, 'Dynamic AMOLED display, multi lens ca,era setup, Wireless Powershare.', 49),
(6, 2, 'S10 Plus', 73000, 'Dynamic AMOLED display, upto 1TB storage, 12GB RAM', 48),
(7, 2, 'S20 Ultra', 98000, '5G, 100x zoom 108MP camera, 16 GB RAM.', 47),
(8, 3, 'OP 7T Pro', 48000, 'Snapdragon 855 plus, 48MP + 16MP + 8MP camera, 8GB RAM, Fluid AMOLED display.', 48),
(9, 3, 'OP 8', 41000, '5G,12GB RAM, Wrap Charge 30T, 12 GB RAM', 47),
(10, 3, 'OP 8 Pro', 50000, '5G, 12GB RAM, 6.78\" display, Fluid AMOLED display, IP68 water resistant.', 47),
(11, 4, 'Pixel 4', 78000, 'Radar, cosmos camera, P-OLED display, Snapdragon 855', 17),
(12, 5, '5.0 Lite', 14500, 'triple camera, 4GB RAM, 48MP camera', 20),
(13, 5, '6.0 Max', 14999, 'Super AMOLED display, in-display fingerprint scanner.', 19),
(14, 6, 'Zenphone 4', 18000, 'AMOLED display, Snapdragon 660', 19),
(15, 6, 'Zenphone 4 Lite', 13999, 'AMOLED display, Snapdragon 630, 4GB RAM', 16),
(16, 7, 'Xperia Z', 20000, 'Snapdragon 550, Quad HD display.', 19),
(17, 2, 'M31', 18990, 'Super AMOLED display, Snapdragon 665, triple camera setup.', 17),
(18, 2, 'M31 Lite', 14990, 'AMOLED display, Snapdragon 660, Wide angle selfie camera.', 17);

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
CREATE TABLE IF NOT EXISTS `sales` (
  `transactionid` int(8) NOT NULL,
  `modelnumber` int(8) NOT NULL,
  `quantity` int(3) NOT NULL,
  `customername` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` bigint(15) NOT NULL,
  `total_bill` float NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`transactionid`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`transactionid`, `modelnumber`, `quantity`, `customername`, `email`, `address`, `phone`, `total_bill`, `date`) VALUES
(1, 1, 1, 'Aman', 'aman@xyz.com', 'Lucknow', 9638527410, 0, '2020-06-15'),
(2, 1, 1, 'Harsh', 'harsh@xyz.com', 'Kanpur', 9863752410, 0, '2020-06-15'),
(3, 2, 1, 'Arpit', 'arpit@xyz.com', 'Kanpur', 9876345120, 0, '2020-06-15'),
(4, 8, 1, 'Harpsh', 'harsh12@xyz.com', 'Gorakhpur', 9632587410, 0, '2020-06-15'),
(5, 13, 1, 'Piyush', 'piyush@xyz.com', 'Lucknow', 9632581470, 0, '2020-06-15'),
(6, 18, 1, 'Anshul', 'anshul@xyz.com', 'Kanpur', 9632580147, 0, '2020-06-15'),
(7, 4, 1, 'Jayant', 'jayant@xyz.com', 'Prayagraj', 9518476230, 0, '2020-06-15'),
(8, 15, 1, 'Aviral', 'aviral@xyz.com', 'Jhasi', 9875321460, 0, '2020-06-15'),
(9, 2, 1, 'Rahul', 'rahul@xyz.com', 'Kanpur', 9514678230, 0, '2020-06-15'),
(10, 8, 1, 'Abhishek', 'abhi@xyz.com', 'Kanpur', 9523614780, 0, '2020-06-15'),
(11, 17, 1, 'Rishab', 'rishu@xyz.com', 'Delhi', 9621354870, 0, '2020-06-15'),
(12, 6, 1, 'Sarthak', 'sarthak@xyz.com', 'Kanpur', 9514236870, 0, '2020-06-15'),
(13, 17, 1, 'Vibhu', 'vibhu@xyz.com', 'Kannauj', 9541236780, 0, '2020-06-15'),
(14, 11, 1, 'Rudhra', 'rudhra@xyz.com', 'Kanpur', 8976453120, 0, '2020-06-15'),
(15, 15, 1, 'Utkarsh', 'utk@xyz.com', 'Kanpur', 7841259630, 0, '2020-06-15'),
(16, 10, 1, 'Arnav', 'arnav@xyz.com', 'Dehradun', 7495681032, 0, '2020-06-15'),
(17, 9, 1, 'Prateek', 'prateek@xyz.com', 'Kanpur', 7412589036, 0, '2020-06-15'),
(18, 18, 1, 'Pushkar', 'pushkar@xyz.com', 'Delhi', 7532146098, 0, '2020-06-15'),
(19, 11, 1, 'Munna', 'munna@xyz.com', 'Mirzapur', 7521468039, 0, '2020-06-15'),
(20, 7, 1, 'Priyanka', 'priya@xyz.com', 'Delhi', 7456329801, 0, '2020-06-15'),
(21, 16, 1, 'Jyoti', 'jyoti@xyz.com', 'Kanpur', 7985130624, 0, '2020-06-15'),
(22, 5, 1, 'Rakesh', 'rakesh@xyz.com', 'Lucknow', 7514298603, 0, '2020-06-15'),
(23, 15, 1, 'Amrit', 'amrit@xyz.com', 'Kanpur', 6745890213, 0, '2020-06-15'),
(24, 2, 1, 'Kartikey', 'kart@xyz.com', 'Kannauj', 6423157809, 0, '2020-06-15'),
(25, 14, 1, 'Yash', 'yash@xyz.com', 'Kanpur', 9521436078, 0, '2020-06-15'),
(26, 6, 1, 'Sirish', 'sirish@xyz.com', 'Kanpur', 8620317945, 0, '2020-06-15'),
(27, 7, 1, 'Ram', 'ram@xyz.com', 'Lucknow', 6841235079, 0, '2020-06-15'),
(28, 17, 1, 'Simran', 'simran@xyz.com', 'Kanpur', 8534012679, 0, '2020-06-15'),
(29, 11, 1, 'Deeptam', 'deep@xyz.com', 'Kanpur', 7456109238, 0, '2020-06-15'),
(30, 9, 1, 'Amrita', 'amrita@xyz.com', 'Kanpur', 8615204937, 0, '2020-06-15'),
(31, 2, 1, 'Prakhar', 'prakhar@xyz.com', 'Lucknow', 9152673840, 0, '2020-06-15'),
(32, 15, 1, 'Ramesh', 'ramesh@xyz.com', 'Kanpur', 7694580231, 0, '2020-06-15'),
(33, 18, 1, 'Abhishek', 'abhishek@xyz.com', 'KAnpur', 6387950214, 0, '2020-06-15'),
(34, 10, 1, 'Ajay', 'ajay@xyz.com', 'Kanpur', 8519463072, 0, '2020-06-15'),
(35, 10, 1, 'Pradumn', 'acp@xyz.com', 'Lucknow', 6198234707, 0, '2020-06-15'),
(36, 7, 1, 'Abhinav', 'abhinav@xyz.com', 'Lucknow', 7185496023, 0, '2020-06-15'),
(37, 9, 1, 'Devansh', 'dev@xyz.com', 'Lucknow', 7388210946, 0, '2020-06-15');

-- --------------------------------------------------------

--
-- Table structure for table `userlogs`
--

DROP TABLE IF EXISTS `userlogs`;
CREATE TABLE IF NOT EXISTS `userlogs` (
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `username` varchar(50) NOT NULL,
  `remarks` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userlogs`
--

INSERT INTO `userlogs` (`timestamp`, `username`, `remarks`) VALUES
('2021-06-27 04:44:40', 'admin', 'Successful'),
('2021-06-27 04:47:13', 'admin', 'Successful'),
('2021-06-27 04:57:32', 'admin', 'Successful');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
