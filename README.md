# WhereTo
https://where2.vercel.app

## Overview
WhereTo is a modern web application that helps users discover and navigate to nearby attractions using their postcode. Built with Next.js and TypeScript, the application integrates multiple APIs to provide a seamless experience for exploring local destinations.

## Screenshots

![Screenshot 2023-12-21 at 2 06 31 PM](https://github.com/joeykyleung/WhereTo/assets/77413460/e758be58-b24a-4123-821a-7c0291ae78c2)
![Screenshot 2023-12-21 at 2 06 37 PM](https://github.com/joeykyleung/WhereTo/assets/77413460/83b4263d-92f4-4809-856f-45caf512af83)

Explore the city like never before by clicking on your favorite attractions, and let our integration with the TFL API guide you seamlessly to your chosen destination.

![Screenshot 2023-12-21 at 2 05 46 PM](https://github.com/joeykyleung/WhereTo/assets/77413460/58f244d9-1483-4f38-af29-294cf6024884)
![Screenshot 2023-12-21 at 2 06 11 PM](https://github.com/joeykyleung/WhereTo/assets/77413460/1a0c0978-191a-4089-a480-8f7b2c7cb927)


## Features
- 🔍 Location-based attraction discovery using postcode
- 🗺️ Interactive map interface with custom markers
- 🚇 Real-time transit directions via TFL API integration
- 📱 Responsive design for mobile and desktop
- 🎨 Modern UI with smooth transitions and animations

## Technical Stack
- **Frontend**: Next.js 13+, TypeScript, Tailwind CSS
- **Maps**: Google Maps API with custom styling
- **Transit Data**: Transport for London (TFL) API
- **Deployment**: Vercel
- **State Management**: React Context API
- **Styling**: CSS Modules with Tailwind

## Technical Challenges & Solutions

### 1. Real-time Transit Integration
- **Challenge**: Integrating TFL API with dynamic route calculations
- **Solution**: Implemented a custom caching layer and error handling for API responses, ensuring reliable transit data delivery even during high-traffic periods

### 2. Map Performance Optimization
- **Challenge**: Handling multiple map markers and state updates efficiently
- **Solution**: Implemented marker clustering and lazy loading of map data to improve performance with large datasets

### 3. Location Data Accuracy
- **Challenge**: Ensuring precise geocoding from postcodes
- **Solution**: Built a validation layer with fuzzy matching to handle various postcode formats and edge cases

## Getting Started

### Prerequisites
- Node.js 16.x or higher
- npm or yarn
- Google Maps API key
- TFL API key

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/WhereTo.git
cd WhereTo
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Create a `.env.local` file with your API keys:
```
NEXT_PUBLIC_GOOGLE_MAPS_API_KEY=your_key_here
NEXT_PUBLIC_TFL_API_KEY=your_key_here
```

4. Start the development server:
```bash
npm run dev
# or
yarn dev
```