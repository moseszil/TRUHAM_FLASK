-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 25, 2026 at 12:42 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `truhamsokogarden`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_description` text DEFAULT NULL,
  `product_cost` int(11) DEFAULT NULL,
  `product_photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES
(1, 'mary land', 'cool and vibrant', 200, 'product1.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `phone`) VALUES
(1, 'Larry Gray', 'L@Gray1', 'glarry@yahoo.com', '+549256365258'),
(2, 'Immaculate Cornnor', 'imma@C55', 'immacornnor@gmail.com', '+155896325222'),
(3, 'Thompson McCaffrey', 'PassWord2s', 'thompsonmccaffrey1@gmail.com', '+912225896646'),
(4, 'Abdul Mohammed', '*MOha254*', 'mohammedabdul@outlook.com', '+254789985225'),
(5, 'Khalid Drakes', 'DkHAlID*1', 'kdrakes@gmail.com', '+254712365478'),
(6, 'Mary', '1234', 'mary@gmail.com', '+2547112233665'),
(7, 'Murray', '1234', 'murray@gmail.com', '+2547123654789'),
(9, 'Immaculate Jane', 'JiMaCute@1', 'jmmaculate@yahoo.com', '+5495886144'),
(10, 'Jamia Cosper', 'JiMa@1', 'cosjamia@yahoo.com', '+2547896554'),
(11, 'Johnkezz Kraze', 'Jkrakes**', 'rakesjk@yahoo.com', '+66987789998'),
(12, 'Sospeter Wachaga', 'peterwachaga@1', 'spwachaga@gmail.com', '+2547123654789'),
(13, 'Elvis Peter Kommen', 'KoMPETR@51', 'epeterkommen@yahoo.com', '+254789666216'),
(14, 'Phoebe Cloe', 'Foorbes**clue', 'phoebecloe@gmail.com', '+65222259986');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
