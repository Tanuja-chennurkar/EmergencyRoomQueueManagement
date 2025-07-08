# Emergency Room Queue Management System

## Overview

This is a Flask-based web application for managing patient queues in a hospital emergency room. The system implements a priority-based queue where patients are prioritized by severity level (1-5, with 1 being highest priority) and arrival time as a tiebreaker. The application provides a simple web interface for adding patients and processing them based on medical priority.

## System Architecture

The application follows a simple MVC (Model-View-Controller) architecture:

- **Model**: `hospital_queue.py` - Contains the core business logic with `Patient` and `EmergencyRoom` classes
- **View**: `templates/index.html` - Web interface for patient management
- **Controller**: `app.py` - Flask routes handling HTTP requests and responses

The architecture prioritizes simplicity and ease of use, making it suitable for small to medium-sized emergency departments.

## Key Components

### Core Classes

1. **Patient Class**
   - Stores patient information (name, age, symptom, severity)
   - Tracks arrival and treatment times
   - Severity scale: 1 (critical) to 5 (minor)

2. **EmergencyRoom Class**
   - Manages the patient queue using a simple list structure
   - Implements priority-based treatment selection
   - Maintains treated patient history

### Web Interface

1. **Flask Application**
   - Three main routes: index, add patient, treat patient
   - Flash messaging for user feedback
   - Form validation for patient data

2. **HTML Template**
   - Bootstrap-based responsive design
   - Dark theme styling
   - Font Awesome icons for visual appeal

## Data Flow

1. **Patient Registration**
   - User submits patient form via web interface
   - Flask validates input data (required fields, numeric types, severity range)
   - New Patient object created and added to queue
   - Success/error message displayed

2. **Patient Treatment**
   - System identifies highest priority patient (lowest severity number)
   - For equal severity, earliest arrival time takes precedence
   - Patient removed from waiting queue
   - Treatment time recorded and patient moved to history
   - Confirmation message displayed

3. **Queue Display**
   - Real-time display of waiting patients
   - Shows patient details and priority information
   - Displays count of treated patients

## External Dependencies

- **Flask**: Web framework for HTTP handling and templating
- **Bootstrap**: CSS framework for responsive UI design
- **Font Awesome**: Icon library for visual elements
- **Python Standard Library**: datetime, os, csv, io modules

No database dependencies - the application uses in-memory storage for simplicity.

## Deployment Strategy

The application is designed for simple deployment scenarios:

- **Development**: Uses Flask's built-in development server
- **Environment Variables**: Supports configurable session secret via `SESSION_SECRET`
- **Static Assets**: Relies on CDN-hosted Bootstrap and Font Awesome
- **No Database Setup**: Eliminates database configuration complexity

The current implementation prioritizes ease of setup over data persistence, making it ideal for development and testing environments.

## Changelog

- July 07, 2025. Initial setup

## User Preferences

Preferred communication style: Simple, everyday language.