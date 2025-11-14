# Service Request Features - Pennsylvania American Water

## 1. Water Quality Request

**Purpose:** Allow customers to report water quality concerns

**Form Fields:**
- Account Number (dropdown - from user's accounts)
- Service Address (auto-filled from selected account)
- Issue Type (dropdown):
  - Discolored Water
  - Unusual Taste
  - Unusual Odor
  - Cloudiness
  - Pressure Issues
  - Other
- Description (text area, optional - "Please describe the issue")
- When did you first notice? (date/time picker)
- Is the issue ongoing? (Yes/No)
- Photo Upload (optional - "Upload up to 3 photos")
- Contact Phone (pre-filled, editable)
- Preferred Contact Method (Phone/Email)

**Submit Button:** "Submit Water Quality Request"

**Confirmation:** Show request number and estimated response time (24-48 hours)

---

## 2. Schedule Service

**Purpose:** Allow customers to request service appointments

**Form Fields:**
- Account Number (dropdown - from user's accounts)
- Service Address (auto-filled from selected account)
- Service Type (dropdown):
  - Meter Reading
  - Meter Repair/Replacement
  - Start Service
  - Stop Service
  - Leak Investigation
  - Other
- Description (text area - "Please describe what you need")
- Preferred Date (date picker - next 30 days)
- Preferred Time (dropdown):
  - Morning (8 AM - 12 PM)
  - Afternoon (12 PM - 5 PM)
  - Any Time
- Alternative Date (date picker, optional)
- Contact Phone (pre-filled, editable)
- Special Instructions (text area, optional)

**Submit Button:** "Request Service Appointment"

**Confirmation:** Show request number and message "We'll contact you within 24 hours to confirm your appointment"

---

## 3. Report Property or Personal Damage

**Purpose:** Allow customers to report damage claims

**Form Fields:**
- Account Number (dropdown - from user's accounts)
- Property Address (text input - where damage occurred)
- Date of Incident (date picker)
- Time of Incident (time picker, optional)
- Type of Damage (dropdown):
  - Property Damage
  - Personal Injury
  - Vehicle Damage
  - Other
- Damage Description (text area - "Describe what happened and the damage")
- Estimated Damage Cost (text input with $ prefix, optional)
- Police/Fire Report Filed? (Yes/No)
- Report Number (text input, shown if Yes selected above)
- Photos/Documents (file upload - "Upload photos and any supporting documents, up to 5 files")
- Contact Phone (pre-filled, editable)
- Contact Email (pre-filled, editable)

**Submit Button:** "Submit Damage Report"

**Confirmation:** Show claim number and message "A claims specialist will contact you within 2 business days. Keep all documentation and photos for your records."

---

## General Features for All Forms

**Common Elements:**
- All forms accessible from main menu under "Customer Service"
- Save draft capability
- Form validation (required fields marked with *)
- Mobile responsive
- Success confirmation page with printable summary
- Email confirmation sent to customer
- Request tracking number for follow-up

**File Upload Requirements:**
- Supported formats: JPG, PNG, PDF
- Max file size: 10MB per file
- Display upload progress
- Preview uploaded files before submit
