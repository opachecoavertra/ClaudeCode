# Feedback & Forms - Pennsylvania American Water

## Overview
Centralized feature for customers to submit feedback, complaints, suggestions, and various forms; track submissions; and view responses.

**Menu Location:** Main Menu > Customer Service > Feedback & Forms

---

## 1. Feedback & Forms Dashboard

### Page Header
- Title: "My Feedback & Submissions"
- "Submit New" button (top right)
- Filter icon

### Quick Stats Cards (Top of page)
- Total Submissions (number)
- Open/Pending (number with orange badge)
- Resolved (number with green badge)
- Avg Response Time (e.g., "2.5 days")

### Filter Options (Slide-out panel)
- Status:
  - All
  - Submitted
  - Under Review
  - In Progress
  - Resolved
  - Closed
- Type:
  - All
  - General Feedback
  - Complaint
  - Suggestion
  - Billing Question
  - Service Quality Issue
  - Water Quality Concern
  - Employee Recognition
  - Other
- Date Range:
  - Last 30 Days
  - Last 90 Days
  - Last Year
  - Custom Range
- Account (if multiple accounts)

### Submission Cards (Mobile) / Table (Desktop)

**Card/Row Display:**
- Submission ID (e.g., FB-2024-12345)
- Status Badge (color coded):
  - Submitted (blue)
  - Under Review (yellow)
  - In Progress (orange)
  - Awaiting Info (purple)
  - Resolved (green)
  - Closed (gray)
- Type Icon + Label
- Subject/Title (truncated)
- Submission Date
- Last Updated
- Response Status:
  - "Response received" (with unread indicator if not viewed)
  - "Awaiting response"
- Quick Actions:
  - View Details
  - Add Information (if awaiting info)

### Empty State
- "No submissions yet"
- "Share your feedback or concerns with us"
- "Submit Feedback" button

---

## 2. Submit New Feedback/Form

### Step 1: Select Type

**Category Cards (Select one):**

**General Feedback**
- Icon: 💬
- Description: "Share your thoughts about our service"

**File a Complaint**
- Icon: ⚠️
- Description: "Report an issue or problem"

**Submit a Suggestion**
- Icon: 💡
- Description: "Help us improve"

**Billing Question**
- Icon: 💵
- Description: "Questions about your bill"

**Service Quality Issue**
- Icon: 🔧
- Description: "Report service concerns"

**Water Quality Concern**
- Icon: 💧
- Description: "Report water quality issues"

**Employee Recognition**
- Icon: ⭐
- Description: "Commend our team members"

**Request Information**
- Icon: ℹ️
- Description: "General inquiries"

### Step 2: Account & Contact Information
- Account Number (dropdown)
- Service Address (auto-filled, display only)
- Your Name (pre-filled, editable)
- Contact Phone (pre-filled, editable)
- Contact Email (pre-filled, editable)
- Preferred Contact Method (dropdown):
  - Email
  - Phone
  - Either

### Step 3: Details Form (Dynamic based on type selected)

#### For General Feedback:
- Subject (text input)
- Category (dropdown):
  - Customer Service Experience
  - Website/App Feedback
  - Communication
  - General Comments
  - Other
- Your Feedback (text area - rich text)
- Related Work Order # (optional)
- Attachments (upload - up to 5 files)

#### For File a Complaint:
- Subject (text input)
- Complaint Category (dropdown):
  - Billing Dispute
  - Service Quality
  - Water Quality
  - Customer Service
  - Property Damage
  - Leak/Infrastructure
  - Outage Response
  - Other
- Priority (auto-set based on category, can override):
  - Low
  - Medium
  - High
  - Urgent
- Date of Incident (date picker)
- Detailed Description (text area)
- What resolution are you seeking? (text area)
- Previous attempts to resolve? (Yes/No)
  - If Yes: Reference Number (text input)
- Photos/Documents (upload - up to 10 files)
- Affected Parties (checkboxes):
  - Just me
  - Multiple households
  - Entire neighborhood

#### For Submit a Suggestion:
- Suggestion Title (text input)
- Area of Improvement (dropdown):
  - Customer Service
  - Billing Process
  - Website/App
  - Conservation Programs
  - Infrastructure
  - Communication
  - Other
- Your Suggestion (text area)
- Expected Benefit (text area - "How would this help?")
- Attachments (optional)

#### For Billing Question:
- Question Type (dropdown):
  - High Bill Inquiry
  - Payment Issue
  - Charge Explanation
  - Budget Billing
  - Payment Plan
  - Other
- Account Number (display)
- Billing Period (dropdown - last 6 months)
- Your Question (text area)
- Upload Bill/Screenshot (optional)

#### For Service Quality Issue:
- Issue Type (dropdown):
  - Low Water Pressure
  - Discoloration
  - Taste/Odor
  - Service Interruption
  - Slow Drainage
  - Other
- When did it start? (date/time picker)
- Is it ongoing? (Yes/No)
- Description (text area)
- Photos/Videos (upload)
- Related to recent work? (Yes/No)
  - If Yes: Work Order # (input)

#### For Water Quality Concern:
- Concern Type (dropdown):
  - Discolored Water
  - Unusual Taste
  - Unusual Odor
  - Cloudiness/Particles
  - Other
- When first noticed? (date/time picker)
- Still occurring? (Yes/No)
- Description (text area)
- Photo Upload (water sample photos)
- Health concerns? (Yes/No checkbox with warning to contact health dept if serious)

#### For Employee Recognition:
- Employee Name (if known)
- Department/Role (if known)
- Date of Interaction (date picker)
- What did they do? (text area)
- How did it help you? (text area)

#### For Request Information:
- Subject (text input)
- Information Requested (text area)
- Related Account/Service (optional)

### Step 4: Review & Submit
- Summary of all entered information
- Checkbox: "I have reviewed my submission and it is accurate"
- Checkbox: "I agree to be contacted regarding this submission"
- Privacy Notice: "Your information is kept confidential per our privacy policy"
- Buttons:
  - Back (to edit)
  - Submit

### Step 5: Confirmation
- Submission ID (large, prominent)
- "Thank you for your submission"
- Expected response timeframe:
  - Complaints: 1-2 business days
  - Feedback: 3-5 business days
  - Suggestions: 5-7 business days
  - Questions: 1-3 business days
- Email confirmation sent notice
- SMS confirmation (if opted in)
- Buttons:
  - View My Submissions
  - Submit Another
  - Return to Dashboard

---

## 3. Submission Details Page

### Header
- Submission ID
- Large Status Badge
- Type Icon + Label
- Print/Download button (PDF)

### Status Timeline
- Submitted (date/time) ✓
- Received (date/time) ✓
- Under Review (date/time, if applicable) ✓
- In Progress (date/time, if applicable)
- Response Sent (date/time, if applicable)
- Resolved (date/time, if applicable)

### Submission Details Card
- Account Number
- Service Address
- Submitted By
- Submission Date
- Category/Type
- Priority (for complaints)
- Subject
- Description
- Attached Files (thumbnails/links to download)

### Status Information Card
- Current Status (with color badge)
- Assigned To (department or person, if applicable)
- Target Response Date
- Last Updated
- Case Manager Contact (if assigned)

### Response & Activity Log

**Company Responses (highlighted):**
- Response date/time
- Responder name/department
- Response message
- Any attached documents/photos
- "Was this helpful?" (Yes/No buttons)

**Status Updates:**
- Timeline of all status changes
- Internal notes (if customer-facing)
- Actions taken

**Customer Updates:**
- Any additional information provided
- Customer replies to responses

### Add Information Section (if requested or customer wants to add)
- "Add Additional Information" button
- Opens modal:
  - Message (text area)
  - Attach files
  - Submit button

### Related Items (if applicable)
- Related Service Orders
- Related Outages
- Related Billing Issues
- Previous Submissions on same topic

### Resolution Section (when resolved)
- Resolution Summary
- Actions Taken
- Final Outcome
- Resolution Date
- Resolved By
- Satisfaction Survey:
  - How satisfied are you with the resolution? (1-5 stars)
  - How satisfied are you with our communication? (1-5 stars)
  - Would you like to provide additional feedback? (optional text area)
  - Submit Feedback button

### Actions (based on status)
- Add Information (if awaiting info)
- Request Update (if no activity in 5+ days)
- Reopen (if closed but issue persists)
- Mark as Resolved (customer confirmation)
- Escalate (if not satisfied with response)

---

## 4. Industry Best Practices Features

### Auto-Categorization & Routing
- Smart detection of urgent issues (keywords like "leak," "no water," "health")
- Auto-route to appropriate department
- Priority assignment based on issue type
- SLA tracking for response times

### Knowledge Base Integration
- "Related Articles" section
- FAQ suggestions based on submission type
- Self-service options before submitting
- "Did this answer your question?" after showing articles

### Sentiment Analysis (Backend)
- Track customer sentiment
- Flag negative sentiment for priority review
- Trend analysis for management dashboard

### Multi-Channel Support
- Submit via web, mobile app
- Option to call and reference submission ID
- Social media integration (reference from Twitter/Facebook)

### Proactive Communication
- Automated acknowledgment within 1 hour
- Status update notifications
- Response alerts
- Escalation notifications if SLA at risk

### Templates & Quick Responses
- Common response templates for staff
- Personalized but efficient responses
- Consistent messaging

### Analytics Dashboard (Customer View)
- "Submission Trends" - personal submission history
- Common issues in your area
- Resolution rate statistics
- Average response times

### Accessibility Features
- Voice-to-text for descriptions
- Screen reader compatible
- Multiple language support
- Large text mode
- High contrast option

---

## 5. Notifications & Communications

### Email Notifications
- Submission confirmed (immediate)
- Status changed
- Response received
- Information requested
- Resolution notification
- Survey invitation

### SMS Notifications (opt-in)
- Submission confirmed
- Response received
- Urgent status changes

### In-App Notifications
- Red badge on Feedback & Forms menu when new responses
- Push notifications for responses

---

## 6. Complaint Escalation Process

### When to Escalate (Auto or Manual)
- No response within SLA
- Customer dissatisfied with resolution
- High priority/urgent issues
- Repeated complaints on same issue

### Escalation Levels
- Level 1: Supervisor Review
- Level 2: Department Manager
- Level 3: Customer Relations Manager
- Level 4: External Ombudsman/Regulatory (if needed)

### Escalation UI
- "Escalate this issue" button (appears after 7 days or if marked unresolved)
- Escalation reason (dropdown):
  - No response received
  - Unsatisfactory response
  - Issue not resolved
  - Need higher authority
- Additional context (text area)
- Submit escalation

### Escalation Confirmation
- Escalation ID
- New review timeframe
- New contact person
- Email to customer and management

---

## 7. Survey & Feedback Forms Library

### Pre-built Survey Templates
- Annual Customer Satisfaction Survey
- Service Experience Survey (post-service order)
- Water Quality Survey
- Conservation Program Feedback
- Website/App Usability Survey
- Community Outreach Feedback

### Survey Features
- Multiple question types (multiple choice, rating, text)
- Progress bar
- Save and continue later
- Anonymous option
- Incentive tracking (if offering rewards for completion)

### Survey Invitation Methods
- Email invitation
- In-app notification
- Post-interaction trigger (after service, payment, etc.)
- Account dashboard banner

---

## 8. UI Design (Following App System Design)

### Status Colors
- Submitted: Blue (#2196F3)
- Under Review: Yellow (#FFC107)
- In Progress: Orange (#FF9800)
- Awaiting Info: Purple (#9C27B0)
- Resolved: Green (#4CAF50)
- Closed: Gray (#9E9E9E)
- Urgent: Red (#F44336)

### Card Layout
- Consistent with service orders and other features
- White background, subtle shadow
- Clear typography hierarchy
- Icon system for quick recognition
- Expandable sections for long content

### Responsive Design
- Mobile: Single column, bottom sheets
- Tablet: Two columns for list/detail
- Desktop: Table view with side panel or modal for details

### Interactive Elements
- Click to expand responses
- Swipe actions (mobile): Mark as read, delete
- Pull to refresh
- Real-time updates when viewing details
- Character counter on text areas
- File upload with drag-and-drop (desktop)

---

## 9. Technical Considerations

### API Endpoints (suggested)
```
GET /api/feedback?accountId={id}&status={status}&type={type}
POST /api/feedback
GET /api/feedback/{id}
PUT /api/feedback/{id}/add-info
POST /api/feedback/{id}/escalate
POST /api/feedback/{id}/satisfaction
GET /api/feedback/{id}/download (PDF)
GET /api/feedback/categories
GET /api/surveys/active
POST /api/surveys/{id}/response
```

### Data Management
- Secure storage of sensitive complaint data
- Audit trail of all actions
- Data retention policy (7 years for complaints per regulations)
- GDPR/privacy compliance for customer data

### Performance
- Pagination (20 submissions per page)
- Lazy load attachments
- Cache static data (categories, templates)
- Search/filter optimization

### Integrations
- CRM system for tracking
- Billing system (for billing-related submissions)
- Service order system (for service issues)
- Water quality monitoring system
- Email/SMS gateway
- Document management system

### Analytics & Reporting (Admin view)
- Submission volume trends
- Response time metrics
- Resolution rates
- Category breakdowns
- Customer satisfaction scores
- Escalation rates
- SLA compliance

---

## 10. Compliance & Regulations

### Water Utility Regulations
- State Public Utility Commission complaint requirements
- EPA water quality complaint procedures
- Customer Bill of Rights display
- Regulatory reporting (quarterly complaint summaries)

### Documentation Requirements
- All complaints logged within 24 hours
- Response within mandated timeframes
- Resolution documentation
- Customer notification of rights

### Privacy & Security
- PII protection
- Secure file uploads
- Access controls
- Data encryption
- Audit logging
