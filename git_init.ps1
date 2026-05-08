# Initializing Git Repository
Write-Host "Navigating to project directory..."
Set-Location -Path "C:\Users\kawinthorn11\Desktop\AssetScanner\FreeAPI_Directory"

Write-Host "Initializing Git..."
git init

Write-Host "Configuring local Git author..."
git config user.email "bot@openclaw.ai"
git config user.name "OpenClaw Asset Scanner"

Write-Host "Adding files to staging area..."
git add .

Write-Host "Creating initial commit..."
git commit -m "Initial commit: Free API Directory parser and backend ready for Vercel"

Write-Host ""
Write-Host "=========================================================="
Write-Host "SUCCESS: Local Git repository initialized and committed."
Write-Host "=========================================================="
Write-Host "Next Steps for Deployment:"
Write-Host "1. Create a new empty repository on GitHub named: free-api-directory"
Write-Host "2. Run the following commands in your terminal:"
Write-Host "   git branch -M main"
Write-Host "   git remote add origin https://github.com/YOUR-USERNAME/free-api-directory.git"
Write-Host "   git push -u origin main"
Write-Host "3. Log into Vercel and import the repository."
Write-Host "=========================================================="