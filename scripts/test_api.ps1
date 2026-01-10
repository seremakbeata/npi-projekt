Write-Host "=== TEST API TO-DO ===" -ForegroundColor Cyan
Write-Host "Data: $(Get-Date)`n" -ForegroundColor Gray

# Test 1: GET
Write-Host "1. GET /tasks" -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "http://localhost:5000/tasks" -Method Get -ErrorAction Stop
    Write-Host "   [OK] GET works" -ForegroundColor Green
} catch {
    Write-Host "   [ERROR] GET failed: $_" -ForegroundColor Red
}

# Test 2: POST
Write-Host "`n2. POST /tasks" -ForegroundColor Yellow
try {
    $body = '{"title": "Test task from PowerShell"}'
    $response = Invoke-RestMethod -Uri "http://localhost:5000/tasks" -Method Post -Body $body -ContentType "application/json" -ErrorAction Stop
    Write-Host "   [OK] POST works (ID: $($response.id))" -ForegroundColor Green
} catch {
    Write-Host "   [ERROR] POST failed: $_" -ForegroundColor Red
}

Write-Host "`n✅ Test completed!" -ForegroundColor Green