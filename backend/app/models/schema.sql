-- FitPulse Database Schema
-- MySQL 8.0, InnoDB, utf8mb4

CREATE DATABASE IF NOT EXISTS fitpulse CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE fitpulse;

-- ============================================================
-- 1. users
-- ============================================================
CREATE TABLE IF NOT EXISTS users (
    id CHAR(36) PRIMARY KEY,
    nickname VARCHAR(50) NOT NULL,
    avatar_url VARCHAR(255) DEFAULT '',
    level ENUM('beginner', 'intermediate', 'advanced') NOT NULL DEFAULT 'beginner',
    goal ENUM('lose_weight', 'build_muscle', 'stay_fit') NOT NULL DEFAULT 'stay_fit',
    equipment JSON,
    weekly_days INT NOT NULL DEFAULT 3,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- ============================================================
-- 2. exercises
-- ============================================================
CREATE TABLE IF NOT EXISTS exercises (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    module ENUM('standard_action', 'muscle_activation', 'error_harm') NOT NULL,
    target_muscles JSON,
    difficulty ENUM('beginner', 'intermediate', 'advanced') NOT NULL DEFAULT 'beginner',
    equipment_needed JSON,
    description TEXT,
    form_cues TEXT,
    breathing TEXT,
    common_errors TEXT,
    image_urls JSON,
    video_url VARCHAR(255) DEFAULT '',
    tags JSON,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_exercises_module (module),
    INDEX idx_exercises_difficulty (difficulty)
) ENGINE=InnoDB;

-- ============================================================
-- 3. knowledge_chunks
-- ============================================================
CREATE TABLE IF NOT EXISTS knowledge_chunks (
    id CHAR(36) PRIMARY KEY,
    chunk_id VARCHAR(100) NOT NULL UNIQUE,
    module ENUM('standard_action', 'muscle_activation', 'error_harm') NOT NULL,
    exercise_id CHAR(36),
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    tags JSON,
    source VARCHAR(255) DEFAULT '',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_kc_module (module),
    INDEX idx_kc_chunk_id (chunk_id),
    FOREIGN KEY (exercise_id) REFERENCES exercises(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- ============================================================
-- 4. training_plans
-- ============================================================
CREATE TABLE IF NOT EXISTS training_plans (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    week_start DATE NOT NULL,
    status ENUM('active', 'completed', 'abandoned') NOT NULL DEFAULT 'active',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE KEY uk_user_week (user_id, week_start)
) ENGINE=InnoDB;

-- ============================================================
-- 5. plan_days
-- ============================================================
CREATE TABLE IF NOT EXISTS plan_days (
    id CHAR(36) PRIMARY KEY,
    plan_id CHAR(36) NOT NULL,
    day_index INT NOT NULL,
    focus VARCHAR(100) DEFAULT '',
    estimated_minutes INT NOT NULL DEFAULT 45,
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (plan_id) REFERENCES training_plans(id) ON DELETE CASCADE,
    UNIQUE KEY uk_plan_day (plan_id, day_index)
) ENGINE=InnoDB;

-- ============================================================
-- 6. plan_exercises
-- ============================================================
CREATE TABLE IF NOT EXISTS plan_exercises (
    id CHAR(36) PRIMARY KEY,
    day_id CHAR(36) NOT NULL,
    exercise_id CHAR(36) NOT NULL,
    sets INT NOT NULL DEFAULT 3,
    reps INT NOT NULL DEFAULT 12,
    rest_seconds INT NOT NULL DEFAULT 60,
    sort_order INT NOT NULL DEFAULT 0,
    FOREIGN KEY (day_id) REFERENCES plan_days(id) ON DELETE CASCADE,
    FOREIGN KEY (exercise_id) REFERENCES exercises(id) ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ============================================================
-- 7. posture_corrections
-- ============================================================
CREATE TABLE IF NOT EXISTS posture_corrections (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    photo_url VARCHAR(255) NOT NULL,
    overall_assessment TEXT,
    safety_note TEXT,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================================
-- 8. correction_issues
-- ============================================================
CREATE TABLE IF NOT EXISTS correction_issues (
    id CHAR(36) PRIMARY KEY,
    correction_id CHAR(36) NOT NULL,
    body_part VARCHAR(50) NOT NULL,
    severity ENUM('mild', 'moderate', 'severe') NOT NULL DEFAULT 'moderate',
    problem TEXT NOT NULL,
    correction TEXT NOT NULL,
    FOREIGN KEY (correction_id) REFERENCES posture_corrections(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================================
-- 9. agent_sessions
-- ============================================================
CREATE TABLE IF NOT EXISTS agent_sessions (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    task_type VARCHAR(50) NOT NULL DEFAULT '',
    context JSON,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================================
-- 10. messages
-- ============================================================
CREATE TABLE IF NOT EXISTS messages (
    id CHAR(36) PRIMARY KEY,
    session_id CHAR(36) NOT NULL,
    role ENUM('user', 'assistant', 'system', 'tool') NOT NULL,
    content TEXT NOT NULL,
    metadata JSON,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES agent_sessions(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================================
-- 11. tool_calls
-- ============================================================
CREATE TABLE IF NOT EXISTS tool_calls (
    id CHAR(36) PRIMARY KEY,
    message_id CHAR(36) NOT NULL,
    tool_name VARCHAR(100) NOT NULL,
    args JSON,
    result JSON,
    FOREIGN KEY (message_id) REFERENCES messages(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ============================================================
-- 12. workout_records
-- ============================================================
CREATE TABLE IF NOT EXISTS workout_records (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    plan_id CHAR(36),
    completed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    duration_minutes INT NOT NULL DEFAULT 0,
    difficulty_rating TINYINT DEFAULT 3,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES training_plans(id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- ============================================================
-- 13. feedbacks
-- ============================================================
CREATE TABLE IF NOT EXISTS feedbacks (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    content TEXT NOT NULL,
    category VARCHAR(50) DEFAULT '',
    status ENUM('pending', 'processing', 'resolved') NOT NULL DEFAULT 'pending',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB;